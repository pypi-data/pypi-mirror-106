from moku import Moku
from moku import session
from moku.exceptions import MokuException
from moku.utilities import find_moku_by_serial
from moku.utilities import validate_range


class Datalogger(Moku):
    """
    Datalogger instrument object.

    Instantiating this class will return a new Datalogger
    instrument with the default state. This may raise a
    :any:`moku.exceptions.InvalidRequestException` if there is an
    active connection to the Moku.

    .. caution::
            Passing force_connect as True will forcefully takeover
            the control of Moku overwriting any existing session.

    """

    def __init__(self, ip=None, serial=None, force_connect=False):
        self.id = 7
        self.operation_group = "datalogger"

        if not any([ip, serial]):
            raise MokuException("IP (or) Serial is required")
        if serial:
            ip = find_moku_by_serial(serial)

        self.session = session.RequestSession(ip)
        super().__init__(force_connect=force_connect, session=self.session)
        self.upload_bitstream(self.id)

    def set_frontend(self, channel, coupling, range, strict=True):
        """
        Configures the input impedance, coupling, and range for each channel.

        :type strict: `boolean`
        :param strict: Disable all implicit conversions and coercions.

        :type channel: `integer`
        :param channel: Target channel

        :type coupling: `string`, {'AC', 'DC'}
        :param coupling: Input Coupling

        :type range: `string`, {'10Vpp', '50Vpp'}
        :param range: Input Range

        """
        operation = "set_frontend"

        params = dict(strict=strict, channel=channel,
                      coupling=validate_range(coupling, list(['AC', 'DC'])),
                      range=validate_range(range, list(['10Vpp', '50Vpp'])),)
        return self.session.post(self.operation_group, operation, params)

    def set_precision_mode(self, state=True, strict=True):
        """
        Changes acquisition mode between 'Normal' and 'Precision'. Precision
        mode is also known as decimation, it samples at the full rate and
        averages excess data points to improve precision. Normal mode works by
        direct down sampling, throwing away extra data points.

        :type strict: `boolean`
        :param strict: Disable all implicit conversions and coercions.

        :type state: `boolean`
        :param state: Change acquisition mode between down sampling and decimation. Precision mode, a.k.a Decimation, samples at full rate and applies a low-pass filter to the data. This improves precision. Normal mode works by direct down sampling, throwing away points it doesn’t need.

        """
        operation = "set_precision_mode"

        params = dict(strict=strict, state=state,)
        return self.session.post(self.operation_group, operation, params)

    def set_samplerate(self, sample_rate, strict=True):
        """
        Sets the sample rate of the instrument.

        :type strict: `boolean`
        :param strict: Disable all implicit conversions and coercions.

        :type sample_rate: `number`, [10, 1e6]
        :param sample_rate: Target samples per second

        """
        operation = "set_samplerate"

        params = dict(strict=strict, sample_rate=sample_rate,)
        return self.session.post(self.operation_group, operation, params)

    def summary(self):
        """
        Returns a short summary of current instrument state.
        """
        operation = "summary"

        return self.session.get(self.operation_group, operation)

    def generate_waveform(
            self,
            channel,
            type,
            amplitude=1,
            frequency=10000,
            offset=0,
            phase=0,
            duty=50,
            symmetry=0,
            dc_level=0,
            edge_time=0,
            pulse_width=0,
            strict=True):
        """
        Configures the output waveform.

        :type strict: `boolean`
        :param strict: Disable all implicit conversions and coercions.

        :type channel: `integer`
        :param channel: Target channel

        :type type: `string`, {'Off', 'Sine', 'Square', 'Ramp', 'Pulse', 'DC'}
        :param type: Waveform type

        :type amplitude: `number`, [4e-3V, 10V]  (defaults to 1)
        :param amplitude: Waveform peak-to-peak amplitude

        :type frequency: `number`, [1e-3Hz, 20e6Hz]  (defaults to 10000)
        :param frequency: Waveform frequency

        :type offset: `number`, [-5V, 5V]  (defaults to 0)
        :param offset: DC offset applied to the waveform

        :type phase: `number`, [0Deg, 360Deg]  (defaults to 0)
        :param phase: Waveform phase offset

        :type duty: `number`, [0.0%, 100.0%]  (defaults to 50)
        :param duty: Duty cycle as percentage (Only for Square wave)

        :type symmetry: `number`, [0.0%, 100.0%]  (defaults to 0)
        :param symmetry: Fraction of the cycle rising

        :type dc_level: `number`
        :param dc_level: DC Level. (Only for DC waveform)

        :type edge_time: `number`, [16e-9, pulse width]  (defaults to 0)
        :param edge_time: Edge-time of the waveform (Only for Pulse wave)

        :type pulse_width: `number`
        :param pulse_width: Pulse width of the waveform (Only for Pulse wave)

        """
        operation = "generate_waveform"

        params = dict(strict=strict,
                      channel=channel,
                      type=validate_range(type,
                                          list(['Off',
                                                'Sine',
                                                'Square',
                                                'Ramp',
                                                'Pulse',
                                                'DC'])),
                      amplitude=amplitude,
                      frequency=frequency,
                      offset=offset,
                      phase=phase,
                      duty=duty,
                      symmetry=symmetry,
                      dc_level=dc_level,
                      edge_time=edge_time,
                      pulse_width=pulse_width,
                      )
        return self.session.post(self.operation_group, operation, params)

    def start_logging(
            self,
            duration=60,
            file_name_prefix="",
            comments="",
            stop_existing=False):
        """
        Start the data logging session to file. The Moku’s internal file system
        is volatile and will be wiped when the Moku is turned off. If you want
        your data logs to persist  move them to a permanent storage location
        before powering your Moku off.

        :type duration: `integer`, Sec (defaults to 60)
        :param duration: Duration to log for

        :type file_name_prefix: `string`
        :param file_name_prefix: Optional file name prefix

        :type comments: `string`
        :param comments: Optional comments to be included

        :type stop_existing: `boolean`
        :param stop_existing: Pass as true to stop any existing session and begin a new one


        .. important::
            It is recommended **not** to relinquish the ownership of the
            device until logging session is completed

        """
        operation = "start_logging"

        params = dict(
            duration=duration,
            file_name_prefix=file_name_prefix,
            comments=comments,
            stop_existing=stop_existing,
        )
        return self.session.post(self.operation_group, operation, params)

    def logging_progress(self):
        """
        Returns current logging state.

        Among available data, 'time_to_end' gives the estimated time
        remaining or 'time_to_start' gives the time remaining to start
        the requested session

        """
        operation = "logging_progress"

        return self.session.get(self.operation_group, operation)

    def stop_logging(self):
        """
        Stops the current instrument data logging session.
        """
        operation = "stop_logging"

        return self.session.get(self.operation_group, operation)
