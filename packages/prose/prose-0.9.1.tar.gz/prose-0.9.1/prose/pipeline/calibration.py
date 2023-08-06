from .. import Sequence, blocks, Block, Image
import os
from os import path
from pathlib import Path
import xarray as xr
from .photometry import plot_function


class Calibration:
    """A calibration unit producing a reduced FITS folder

    The calibration encompass more than simple flat, dark and bias calibration. It contains two sequences whose ...
    TODO

    Parameters
    ----------
    destination : str, optional
        Destination of the newly created folder, by default beside the folder given to FitsManager
    reference : float, optional
        Reference image to use for alignment from 0 (first image) to 1 (last image), by default 1/2
    overwrite : bool, optional
        whether to overwrite existing products, by default False
    flats : list, optional
        list of flats images paths, by default None
    bias : list, optional
        list of bias images paths, by default None
    darks : list, optional
        list of darks images paths, by default None
    images : list, optional
        list of images paths to be calibrated, by default None
    psf : `Block`, optional
        a `Block` to be used to characterise the effective psf, by default blocks.Moffat2D
    show: bool, optional
        within a notebook, whether to show processed image during reduction, by default False 
    verbose: bool, optional
        whether to print processing info and loading bars, by default True
    twirl: bool, optional,
        whether to use the Twirl block for alignment (see blocks.registration.Twirl)
    n: int, optional,
        number of stars used for alignment, by default None leading to 12 if twirl else 50
    loader: Image class, optional
        class to load Images, by default Image
    """

    def __init__(
            self,
            reference=1/2,
            overwrite=False,
            flats=None,
            bias=None,
            darks=None,
            images=None,
            psf=blocks.Moffat2D,
            verbose=True,
            show=False,
            twirl=True,
            n=None,
            loader=Image,
    ):
        self.destination = None
        self.overwrite = overwrite
        self._reference = reference
        self.verbose = verbose
        self.show = show
        self.n = n if n is not None else (12 if twirl else 50)
        self.twirl = twirl

        if show:
            self.show = blocks.LivePlot(plot_function, size=(10, 10))
        else:
            self.show = blocks.Pass()

        self.flats = flats
        self.bias = bias
        self.darks = darks
        self._images = images
        self.loader = loader

        self.detection_s = None
        self.calibration_s = None

        assert psf is None or issubclass(psf, Block), "psf must be a subclass of Block"
        self.psf = psf
        
        # set reference file
        reference_id = int(self._reference * len(self._images))
        self.reference_fits = self._images[reference_id]
        self.calibration_block = blocks.Calibration(self.darks, self.flats, self.bias, loader=loader, name="calibration")

    def run(self, destination, gif=True):
        """Run the calibration pipeline

        Parameters
        ----------
        destination : str
            Destination where to save the calibrated images folder
        """
        self.destination = destination
        gif_block = blocks.Video(self.gif_path, name="video", from_fits=True) if gif else blocks.Pass()

        self.make_destination()

        self.detection_s = Sequence([
            self.calibration_block,
            blocks.Trim(name="trimming"),
            blocks.SegmentedPeaks(n_stars=self.n, name="detection"),
            blocks.ImageBuffer(name="buffer")
        ], self.reference_fits, loader=self.loader)

        self.detection_s.run(show_progress=False)

        ref_image = self.detection_s.buffer.image
        ref_stars = ref_image.stars_coords

        self.calibration_s = Sequence([
            self.calibration_block,
            blocks.Trim(name="trimming", skip_wcs=True),
            blocks.Flip(ref_image, name="flip"),
            blocks.SegmentedPeaks(n_stars=self.n, name="detection"),
            blocks.Twirl(ref_stars, n=self.n, name="twirl") if self.twirl else blocks.XYShift(ref_stars),
            self.psf(name="fwhm"),
            blocks.Cutout2D(ref_image) if not self.twirl else blocks.Pass(),
            blocks.SaveReduced(self.destination, overwrite=self.overwrite, name="save_reduced"),
            blocks.AffineTransform(stars=True, data=True) if self.twirl else blocks.Pass(),
            self.show,
            blocks.Stack(self.stack_path, header=ref_image.header, overwrite=self.overwrite, name="stack"),
            blocks.Video(self.gif_path, name="video", from_fits=True),
            blocks.XArray(
                ("time", "jd_utc"),
                ("time", "bjd_tdb"),
                ("time", "flip"),
                ("time", "fwhm"),
                ("time", "fwhmx"),
                ("time", "fwhmy"),
                ("time", "dx"),
                ("time", "dy"),
                ("time", "airmass"),
                ("time", "exposure")
            )
        ], self._images, name="Calibration", loader=self.loader)

        self.calibration_s.run(show_progress=self.verbose)

        # saving xarray
        calib_xarray = self.calibration_s.xarray.xarray
        stack_xarray = self.calibration_s.stack.xarray
        xarray = xr.merge([calib_xarray, stack_xarray], combine_attrs="no_conflicts")
        xarray = xarray.assign_coords(time=xarray.jd_utc)
        xarray.attrs["time_format"] = "jd_utc"
        xarray.attrs["reduction"] = [b.__class__.__name__ for b in self.calibration_s.blocks]
        xarray.to_netcdf(self.phot_path)

    @property
    def stack_path(self):
        return self.destination / "stack.fits"

    @property
    def phot_path(self):
        return self.destination / (self.destination.name + ".phot")

    @property
    def stack(self):
        return self.stack_path

    @property
    def images(self):
        return self.calibration_s.save_reduced.files

    @property
    def gif_path(self):
        prepend = "movie.gif"
        return path.join(self.destination, prepend)

    @property
    def processing_time(self):
        return self.calibration_s.processing_time + self.detection_s.processing_time

    def make_destination(self):
        self.destination = Path(self.destination)
        self.destination.mkdir(exist_ok=True)
        if not path.exists(self.destination):
            os.mkdir(self.destination)

    def __repr__(self):
        return f"{self.detection_s}\n{self.calibration_s}"

    @property
    def xarray(self):
        return self.calibration_s.xarray()

