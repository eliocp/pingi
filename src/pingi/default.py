from typing import ClassVar


class DefaultParams:
    """
    A class that defines default values for the parameters of the configuration, plot
    and annotation functions.

    Class Parameters
    ----------------

    fontsize_factor : float, default=1.0
        Default multiplication factor for the size of all fonts considered in the
        visualization functions.
    """

    fontsize_factor: ClassVar[float] = 1.0

    @classmethod
    def set_fontsize_factor(cls, value: float) -> None:
        """
        Set `fontsize_factor` (default multiplication factor for the size of all fonts
        considered in the visualization functions).

        Parameters
        ----------
        value : float
            The value to set.
        """
        cls.fontsize_factor = value

    @classmethod
    def get_fontsize_factor(cls) -> float:
        """
        Get `fontsize_factor` (default multiplication factor for the size of all fonts
        in the visualization functions).

        Returns
        -------
        float
            The value of `fontsize_factor`.
        """
        return cls.fontsize_factor
