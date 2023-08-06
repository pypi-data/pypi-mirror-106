
"""
Communication with the LUUP engine on a MiCasaVerde Vera device.

To use, either initialise a VeraRemote or VeraLocal object, or use the
connect function.

>>> import vera
>>>
>>> # Remote connection
>>> device_id = 45191949
>>> ve = vera.VeraRemote("user", "password", device_id)
Account number: 100000
Server device: vera-us-oem-device12.mios.com
Server relay: vera-us-oem-relay41.mios.com
Connected to remote device.
>>>
>>> # Local connection
>>> ve = vera.VeraLocal("192.168.0.10")
>>>
>>> open("LUUP-AUTH.json","r").read()
{
  "remote": {
    "user": "user",
    "password": "password",
    "device": "49876656"
  }
}
>>> ve = vera.connect()
Account number: 100000
Server device: vera-us-oem-device12.mios.com
Server relay: vera-us-oem-relay41.mios.com
Connected to remote device.
"""

from . color import *
import json
import sys
import hashlib
import base64
import time
import requests

# Reverse-engineered by looking at icons at
# http://.../cmh/skins/default/img/icons/{code}.png
weather_types = {
    0: "hurricane",
    1: "cyclone",
    2: "heavy-cyclone",
    3: "thunderstorm",
    4: "thunderstorm",
    5: "sleet",
    6: "sleet",
    7: "heavy-sleet",
    8: "freezing-rain",
    9: "hailstorm",
    10: "freezing-rain",
    11: "rain",
    12: "heavy-hailstorm",
    13: "heavy-snow",
    14: "snow",
    15: "hailstorm",
    16: "heavy-snow",
    17: "hail",
    18: "heavy-sleet",
    19: "windy",
    20: "fog",
    21: "mist",
    22: "cloudy",
    23: "windy",
    24: "solar-eclipse",
    25: "freeze",
    26: "cloudy",
    27: "partly-cloudy",
    28: "sunny-intervals",
    29: "clear-intervals",
    30: "sunny-intervals",
    31: "clear-night",
    32: "sun",
    33: "clear-night",
    34: "sun",
    35: "sleet",
    36: "heatwave",
    37: "thunderstorm",
    38: "thunderstorm",
    39: "thunderstorm",
    40: "rainstorm",
    41: "snowstorm",
    42: "snowstorm",
    43: "snowstorm",
    44: "heavy-cloud",
    45: "thunderstorm",
    46: "snow",
    47: "heavy-thunderstorm"
}

class Time(object):
    """
    Time object represents a time value in a 24-hour day i.e. a value
    we might normally represent HH:MM:SS.
    """

    def __init__(self, h=0, m=0, s=0, after_sunrise=False, after_sunset=False):
        """
        Constructs a new Time object.
        :param h: Hour value
        :param m: Minute value
        :param s: Seconds value
        :param after_sunrise: True if value is relative to sunrise
        :param after_sunset: True if the time value is relative to sunset
        """
        assert (after_sunrise and after_sunset) == False, \
            "Must not specify both after_sunrise and after_sunset"
#        assert isinstance(h, int), "h must be integer"
#        assert isinstance(m, int), "m must be integer"
#        assert isinstance(s, int), "s must be integer"
        
        self.time = (h, m, s)
        self.after_sunrise = after_sunrise
        self.after_sunset = after_sunset

    def output(self):
        """
        Formats the time value in a format suitable for LUUP comms.
        """
        if self.after_sunrise:
            return "%02d:%02d:%02dR" % self.time
        if self.after_sunset:
            return "%02d:%02d:%02dT" % self.time
        return "%02d:%02d:%02d" % self.time

    @staticmethod
    def parse(s):
        """
        Converts LUUP time values to a Time object.

        :param s: Value from LUUP comms.
        """

        rise = False
        set = False
        if s[-1:] == "R":
            rise = True
            s = s[:-1]
        elif s[-1:] == "T":
            set = True
            s = s[:-1]
        
        x = s.split(":")
        if len(x) == 1:
            x.append("0")
        if len(x) == 2:
            x.append("0")
        
        return Time(int(x[0]), int(x[1]), int(x[2]), after_sunrise=rise,
                    after_sunset=set)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        return self.__dict__ == obj.__dict__ and type(self) == type(obj)

class Timer(object):
    """
    Base class for a timer value.  There are four types of timer
    implemented in the four subclasses.
    """

    @staticmethod
    def parse(s):
        """
        Converts LUUP timer values to a Timer object.

        :param s: Value from LUUP comms.
        """

        if s["type"] == 1:
            return IntervalTimer.parse(s)

        if s["type"] == 2:
            return DayOfWeekTimer.parse(s)

        if s["type"] == 3:
            return DayOfMonthTimer.parse(s)

        if s["type"] == 4:
            return AbsoluteTimer.parse(s)

        raise RuntimeError("Parsing timer not implemented.")

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        return self.__dict__ == obj.__dict__

class DayOfWeekTimer(Timer):
    """
    Represents a daily timer which fires at a specific point in a
    24-hour day.  The timer can be restricted so that it only operates on
    certain days in the week.
    """

    def __init__(self, id=None, name=None, days=None, time=None):
        """
        Creates a DayOfWeekTimer object.

        :param id: Integer identifier for the timer.
        :param name: A human-readable name.
        :param days: A string containing comma-separated digits representing
        the days of the week, 1=Monday etc.
        :param time: A Time object representing the time.
        """

#        assert isinstance(days, list), "days should be a list of integers"
#        assert all(isinstance(elt, int) for elt in days), "days should be list of integers"
#        assert all(1 <= elt <= 7 for elt in days), "days elements should be 1-7"

        self.id = id
        self.name = name
        self.days = days
        self.time = time

    def output(self):
        """
        Formats the time value in a format suitable for LUUP comms.
        """
        return {
            "id": self.id,
            "name": self.name,
            "type": 2,
            "enabled": 1,
            "days_of_week": self.days,
            "time": self.time.output()
       }

    @staticmethod
    def parse(s):
        """
        Converts LUUP day-of-week timer values to a DayOfWeekTimer object.

        :param s: Value from LUUP comms.
        """
        t = DayOfWeekTimer()
        t.id = s.get("id", None)
        t.name = s.get("name", None)
        t.days = s.get("days_of_week", None)
        if "time" in s:
            t.time = Time.parse(s["time"])
        else:
            t.time = None
        return t
    
class DayOfMonthTimer(Timer):
    """
    Represents a daily timer which fires at a specific point in a
    24-hour day.  The timer can be restricted so that it only operates on
    certain days in the month.
    """

    def __init__(self, id=None, name=None, days=None, time=None):
        """
        Creates a new DayOfMonthTimer.

        :param id: Integer identifier for the timer.
        :param name: A human-readable name.
        :param days: A string containing comma-separated digits representing
        the days of the month, 1=1st etc.
        :param time: A Time object representing the time.
        """
#        assert isinstance(days, list), "days should be a list of integers"
#        assert all(isinstance(elt, int) for elt in days), "days should be list of integers"
#        assert all(1 <= elt <= 31 for elt in days), "days elements should be 1-31"

        self.id = id
        self.name = name
        self.days = days
        self.time = time

    def output(self):
        """
        Formats the time value in a format suitable for LUUP comms.
        """
        return {
            "id": self.id,
            "name": self.name,
            "type": 3,
            "enabled": 1,
            "days_of_month": self.days,
            "time": self.time.output()
        }

    @staticmethod
    def parse(s):
        """
        Converts LUUP day-of-month timer values to a DayOfMonthTimer object.

        :param s: Value from LUUP comms.
        """
        t = DayOfMonthTimer()
        t.id = s.get("id", None)
        t.name = s.get("name", None)
        t.days = s.get("days_of_month", None)
        if "time" in s:
            t.time = Time.parse(s["time"])
        else:
            t.time = None
        return t
    
class IntervalTimer(Timer):
    """
    A timer describing a regularly occuring event, whose period can be
    described in terms of a number of seconds, minutes, hours or days.
    """
    
    def __init__(self, id=None, name=None, seconds=0, minutes=0, hours=0,
                 days=0):
        """
        Create a new IntervalTimer object.

        :param id: Integer identified for timer.
        :param name: Human-readable name for the timer.
        :param seconds: Interval value in seconds.
        :param minutes: Interval value in minutes.
        :param hours: Interval value in hours.
        :param days: Interval value in days.

        """

        specd = 0
        if seconds != 0: specd = specd + 1
        if minutes != 0: specd = specd + 1
        if hours != 0: specd = specd + 1
        if days != 0: specd = specd + 1

        assert specd < 2, \
            "Should specify only one of seconds, minutes, hours and days"

        self.id = id
        self.name = name
        (self.seconds, self.minutes, self.hours, self.days) = \
            (seconds, minutes, hours, days)

    def output(self):
        """
        Formats the value in a format suitable for LUUP comms.
        """
        
        if self.days > 0:
            interval = "%dd" % self.days
        if self.hours > 0:
            interval = "%dh" % self.hours
        if self.minutes > 0:
            interval = "%dm" % self.minutes
        else:
            interval = "%ds" % self.seconds
        
        return {
            "id": self.id,
            "name": self.name,
            "type": 1,
            "enabled": 1,
            "interval": interval
        }

    @staticmethod
    def parse(s):
        """
        Converts LUUP interval timer values to a IntervalTimer object.

        :param s: Value from LUUP comms.
        """
        t = IntervalTimer()
        t.id = s.get("id", None)
        t.name = s.get("name", None)
        if "interval" in s:
            ival = s["interval"]
            if ival[-1:] == "s":
                t.seconds = int(ival[:-1])
            if ival[-1:] == "m":
                t.minutes = int(ival[:-1])
            if ival[-1:] == "h":
                t.hours = int(ival[:-1])
            if ival[-1:] == "d":
                t.days = int(ival[:-1])
        return t
    
class AbsoluteTimer(Timer):
    """
    Describes a timer which fires only once, at a described point in time.
    """

    def __init__(self, id=None, name=None, year=None, month=None, date=None,
                 hours=0, minutes=0, seconds=0):
        """
        Creates an AbsoluteTimer object.

        :param id: Identified for the timer.
        :param name: Human-readble name for the timer.
        :param year: Absolute year value, 4-digit.
        :param month: Absolute month value, 1-12.
        :param date: Absolute date value, 1-31.
        :param hours: Hour value.
        :param minutes: Minute value.
        :param seconds: Seconds value.
        """
        self.id, self.name = id, name
        (self.year, self.month, self.date) = (year, month, date)
        (self.hours, self.minutes, self.seconds) = (hours, minutes, seconds)

    def output(self):
        """
        Formats the timer value in a format suitable for LUUP comms.
        """
        time = "%04d-%02d-%02d %02d:%02d:%02d" % (self.year, self.month, \
                self.date, self.hours, self.minutes, self.seconds)
        return {
            "id": self.id,
            "name": self.name,
            "type": 4,
            "enabled": 1,
            "abstime": time
        }

    @staticmethod
    def parse(s):
        """
        Converts LUUP absolute timer values to an AbsoluteTimer object.

        :param s: Value from LUUP comms.
        """

        t = AbsoluteTimer()
        t.id = s.get("id", None)
        t.name = s.get("name", None)
        
        if "abstime" in s:

            parts = s["abstime"].split(" ")

            if len(parts) != 2:
                raise RuntimeError("Invalid date format")

            dateparts = parts[0].split("-")
            timeparts = parts[1].split(":")
            
            if len(dateparts) != 3:
                raise RuntimeError("Invalid date format")
            if len(timeparts) != 3:
                raise RuntimeError("Invalid date format")

            t.year = int(dateparts[0])
            t.month = int(dateparts[1])
            t.date = int(dateparts[2])
            t.hours = int(timeparts[0])
            t.minutes = int(timeparts[1])
            t.seconds = int(timeparts[2])

        return t
    
class Trigger(Timer):
    """
    Describes a device-initiated event for triggering a scene.
    """
    
    def __init__(self, id=None, name=None, device=None, template=None,
                 args=None, start=None, stop=None, days_of_week=None):
        """
        Creates a Trigger object.

        :param id: Trigger identifier.
        :param name: Human-readable name.
        :param device: Device object identifying the device which is to
        initiate the scene
        :param template: is the template function for the device
        :param args: is a sequence of arguments
        :param start: a Time object specifying the start time for the period
        for which this trigger is valid.
        :param end: a Time object specifying the end time for which this trigger
        is valid
        :param days_of_week: days for which this trigger applies.
        """
        self.id, self.name = id, name
        self.device = device
        self.template = template
        if args == None:
            self.args = []
        else:
            self.args = args
        self.start, self.stop = start, stop
        self.days_of_week = days_of_week

    def output(self):
        """
        Formats the value in a format suitable for LUUP comms.
        """
        args = []
        for i in range(0, len(self.args)):
            args.append({"id": i + 1, "value": self.args[i]})

        val = {
            "id": self.id,
            "device": self.device.id,
            "enabled": 1,
            "name": self.name,
            "template": self.template,
            "arguments": args
        }

        if self.start != None and self.stop != None:
            val["start"] = self.start.output()
            val["stop"] = self.stop.output()

        if self.days_of_week != None:
            val["days_of_week"] = self.days_of_week

        return val

    @staticmethod
    def parse(vera, s):
        """
        Converts LUUP trigger values to a Trigger object.

        :param vera: Vera object.
        :param s: Value from LUUP comms.
        """

        t = Trigger()

        t.id = s.get("id", None)
        t.template = s.get("template", None)
        t.name = s.get("name", None)
        t.days_of_week = s.get("days_of_week", None)
        
        if "arguments" in s:
            for i in s["arguments"]:
                if 'value' in i:
                    t.args.append(i["value"])

        if "device" in s:
            t.device = vera.get_device_by_id(s["device"])
        else:
            t.device = None

        if "start" in s:
            t.start = Time.parse(s["start"])
        else:
            t.start = None

        if "stop" in s:
            t.stop = Time.parse(s["stop"])
        else:
            t.stop = None

        return t

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        return self.__dict__ == obj.__dict__ and type(self) == type(obj)

class Job(object):
    """
    Represents a job, typically used to implement an action.
    """
    def __init__(self):
        """
        Creates a Job object.
        """
        pass

    def get_status(self):
        """
        Gets the job status, returns a tuple.  First element is job code,
        second element is human-readable meaning of the job code.
        """
        url = "data_request?id=jobstatus&job=%d&plugin=zwave" % self.id
        return self.vera.get(url)

    def is_complete(self):
        """
        Tests whether the job has completed.
        :return: True if the job is complete, False otherwise.
        """
        status = self.get_status()
        return status["status"] == 4
    
    def is_pending(self):
        """
        Tests whether the job is stilling pending completion.
        :return: True if the job is still pending completion, False otherwise.
        """
        status = self.get_status()
        return status["status"] == 3
    
    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        if type(self) != type(obj): return False
        return self.__dict__ == obj.__dict__

class Action(object):
    """
    Base class describing an action.
    """

    def invoke(self):
        """
        Invoke an action
        :return: a Job object, describing the job implementing the action.
        """
        raise RuntimeError("Not implemented")

    @staticmethod
    def parse(vera, s):
        """
        Converts LUUP action values to an Action object.

        :param vera: A Vera object.
        :param s: Value from LUUP comms.
        """

        if s["service"] == "urn:upnp-org:serviceId:TemperatureSetpoint1":
            return SetpointAction.parse(vera, s)

        if s["service"] == "urn:upnp-org:serviceId:Dimming1":
            return DimmerAction.parse(vera, s)

        if s["service"] == "urn:upnp-org:serviceId:SwitchPower1":
            return SwitchAction.parse(vera, s)

        if s["service"] == "urn:upnp-org:serviceId:HVAC_UserOperatingMode1":
            return HeatingAction.parse(vera, s)

        if s["service"] == "urn:upnp-org:serviceId:RGBController1":
            return RGBAction.parse(vera, s)

        if s["service"] == "urn:micasaverde-com:serviceId:Color1":
            return ColorAction.parse(vera, s)

        raise RuntimeError("Don't know how to handle service %s" %
                           s["service"])

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        return self.__dict__ == obj.__dict__ and type(self) == type(obj)

class SetpointAction(Action):
    """
    An action, which changes the 'set point' of a thermostat.

    Note that when this action is applied to a battery-powered device, the
    result may not be applied until the device does a rendezvous with the
    controller.
    """

    def __init__(self, device=None, value=None):
        """
        Creates a SetpointAction object.
        :param device: Device object specifying the device
        :param value: set-point value, a float
        """
        self.device = device
        self.value = value

    def output(self):
        """
        Formats the value in a format suitable for LUUP comms.
        """
        return {
            "device": self.device.id, 
            "action": "SetCurrentSetpoint", 
            "arguments": [
                {
                    "name": "NewCurrentSetpoint", 
                    "value": self.value
                }
            ], 
            "service": "urn:upnp-org:serviceId:TemperatureSetpoint1"
        }

    def invoke(self):
        """
        Immediately invoke the action
        :return: a Job object, describing the job implementing the action.
        """
        base="data_request?id=action"
        action = "SetCurrentSetpoint"
        svc = "urn:upnp-org:serviceId:TemperatureSetpoint1"
        path = "%s&DeviceNum=%d&serviceId=%s&action=%s&NewCurrentSetpoint=%f&output_format=json" \
               % (base, self.device.id, svc, action, self.value)
        status = self.device.vera.get(path)

        job = Job()
        job.id = int(status["u:SetCurrentSetpointResponse"]["JobID"])
        job.vera = self.device.vera
        return job

    @staticmethod
    def parse(vera, s):
        """
        Converts LUUP SetCurrentSetpoint action values to a SetpointAction
        object.

        :param s: Value from LUUP comms.
        """
        ha = SetpointAction()
        ha.device = vera.get_device_by_id(s["device"])
        ha.value = s["arguments"][0]["value"]
        return ha

class SwitchAction(Action):
    """
    Action which operates against a standard power switch which has on/off
    semantics.
    """

    def __init__(self, device=None, value=None):
        """
        Creates a SwitchAction object.
        :param device: Device object describing the device to apply
        :param value: boolean value for switch
        """
        self.device = device
        self.value = value

    def output(self):
        """
        Formats the value in a format suitable for LUUP comms.
        """
        return {
            "device": self.device.id, 
            "action": "SetTarget",
            "arguments": [
                {
                    "name": "newTargetValue", 
                    "value": self.value
                }
            ], 
            "service": "urn:upnp-org:serviceId:SwitchPower1"
        }

    def invoke(self):
        """
        Implements the defined action.
        :return: a Job object, describing the job implementing the action.
        """

        if self.value:
            value = 1
        else:
            value = 0

        base="data_request?id=action"
        action = "SetTarget"
        svc = "urn:upnp-org:serviceId:SwitchPower1"
        path = "%s&DeviceNum=%d&serviceId=%s&action=%s&newTargetValue=%d&output_format=json" \
               % (base, self.device.id, svc, action, value)
        status = self.device.vera.get(path)

        job = Job()

        # Sometimes get a buggy response
        try:
            job.id = int(status["u:SetTargetResponse"]["JobID"])
        except:
            job.id = int(status["u:SetLoadLevelTargetResponse"]["JobID"])
        job.vera = self.device.vera
        return job

    @staticmethod
    def parse(vera, s):
        """
        Converts LUUP SetTarget values to a SwitchAction object.

        :param s: Value from LUUP comms.
        """
        ha = SwitchAction()
        ha.device = vera.get_device_by_id(s["device"])
        ha.value = s["arguments"][0]["value"]
        return ha

class DimmerAction(Action):
    """
    Action which changes the dim level of a dimmer device
    """

    def __init__(self, device=None, value=None):
        """
        Creates a DimmerAction object.
        
        :param device: a Device object specifying the device to be affected
        :param value: Dim value, integer 0-100
        """
        self.device = device
        self.value = value

    def output(self):
        """
        Formats the value in a format suitable for LUUP comms.
        """
        return {
            "device": self.device.id, 
            "action": "SetLoadLevelTarget", 
            "arguments": [
                {
                    "name": "newLoadlevelTarget", 
                    "value": self.value
                }
            ], 
            "service": "urn:upnp-org:serviceId:Dimming1"
        }

    def invoke(self):
        """
        Invokes the action, affecting the specified device.
        :return: a Job object, describing the job implementing the action.
        """

        base="data_request?id=action"
        action = "SetLoadLevelTarget"
        svc = "urn:upnp-org:serviceId:Dimming1"
        path = "%s&DeviceNum=%d&serviceId=%s&action=%s&newLoadlevelTarget=%d&output_format=json" \
               % (base, self.device.id, svc, action, self.value)
        status = self.device.vera.get(path)

        job = Job()
        job.id = int(status["u:SetLoadLevelTargetResponse"]["JobID"])
        job.vera = self.device.vera
        return job

    @staticmethod
    def parse(vera, s):
        """
        Converts LUUP values to a DimmerAction object.

        :param s: Value from LUUP comms.
        """
        ha = DimmerAction()
        ha.device = vera.get_device_by_id(s["device"])
        ha.value = s["arguments"][0]["value"]
        return ha

class HeatingAction(Action):
    """
    Action which changes the operational mode of a heating device
    """

    def __init__(self, device=None, value=None):
        """
        Creates a HeatingAction device.

        :param device: a Device object specifying the device to be affected
        :param value: string, one of: Off, HeatOn
        """
        self.device = device
        self.value = value

    def output(self):
        """
        Formats the time value in a format suitable for LUUP comms.
        """
        return {
            "device": self.device.id, 
            "action": "SetModeTarget", 
            "arguments": [
                {
                    "name": "NewModeTarget", 
                    "value": self.value
                }
            ], 
            "service": "urn:upnp-org:serviceId:HVAC_UserOperatingMode1"
        }

    def invoke(self):
        """
        Invokes the action, affecting the specified device.
        :return: a Job object, describing the job implementing the action.
        """

        base="data_request?id=action"
        action = "SetModeTarget"
        svc = "urn:upnp-org:serviceId:HVAC_UserOperatingMode1"
        path = "%s&DeviceNum=%d&serviceId=%s&action=%s&NewModeTarget=%s&output_format=json" \
               % (base, self.device.id, svc, action, self.value)
        status = self.device.vera.get(path)

        job = Job()
        job.id = int(status["u:SetModeTargetResponse"]["JobID"])
        job.vera = self.device.vera
        return job

    @staticmethod
    def parse(vera, s):
        """
        Converts LUUP values to a HeatingAction object.

        :param s: Value from LUUP comms.
        """
        ha = HeatingAction()
        ha.device = vera.get_device_by_id(s["device"])
        ha.value = s["arguments"][0]["value"]
        return ha

class RGBAction(Action):
    """
    Action which operates against a colour controller which has 5 channels
    """

    def __init__(self, device=None, color=None):
        """
        Creates a RGBAction object.
        :param device: Device object describing the device to apply
        :param color: value for color, should be an RGB, Daylight or Warm object
        """
        self.device = device
        self.color = color

    def output(self):
        """
        Formats the value in a format suitable for LUUP comms.
        """
        h = self.color.to_hex()

        return {
            "device": self.device.id, 
            "action": "SetColor",
            "arguments": [
                {
                    "name": "newColorTargetValue", 
                    "value": str(self.color)
                }
            ], 
            "service": "urn:upnp-org:serviceId:RGBController1"
        }

    def invoke(self):
        """
        Implements the defined action.
        :return: a Job object, describing the job implementing the action.
        """

        base="data_request?id=action"
        action = "SetColorTarget"
        svc = "urn:upnp-org:serviceId:RGBController1"
        path = "%s&DeviceNum=%d&serviceId=%s&action=%s&newColorTargetValue=%s&transitionDuration=0&transitionNbSteps=10&output_format=json" \
               % (base, self.device.id, svc, action, self.color.to_hex())
        status = self.device.vera.get(path)
        job = Job()
        job.id = int(status["u:SetColorTargetResponse"]["JobID"])
        job.vera = self.device.vera
        return job

    @staticmethod
    def parse(vera, s):
        """
        Converts LUUP SetTarget values to a RGBAction object.

        :param s: Value from LUUP comms.
        """
        sa = RGBAction()
        sa.device = vera.get_device_by_id(s["device"])
        value = s["arguments"][0]["value"]
        sa.color = Color.parse(value)
        return sa

class ColorAction(Action):
    """
    Action which operates against a colour controller which has color channels
    """

    def __init__(self, device=None, color=None):
        """
        Creates a ColorAction object.
        :param device: Device object describing the device to apply
        :param value: value for color
        """
        self.device = device
        self.color = color

    def output(self):
        """
        Formats the value in a format suitable for LUUP comms.
        """

        if isinstance(self.color, Daylight):
            return {
                "device": self.device.id, 
                "action": "SetColor",
                "arguments": [
                    {
                        "name": "newColorTarget", 
                        "value": str(self.color)
                    }
                ],
                "service": "urn:micasaverde-com:serviceId:Color1"
            }
        elif isinstance(self.color, Warm):
            return {
                "device": self.device.id, 
                "action": "SetColor",
                "arguments": [
                    {
                        "name": "newColorTarget", 
                        "value": str(self.color)
                    }
                ],
                "service": "urn:micasaverde-com:serviceId:Color1"
            }
        elif isinstance(self.color, RGB):
            return {
                "device": self.device.id, 
                "action": "SetColorRGB",
                "arguments": [
                    {
                        "name": "newColorRGBTarget", 
                        "value": "%d,%d,%d" % self.color.value
                    }
                ],
                "service": "urn:micasaverde-com:serviceId:Color1"
            }
        else:
            raise RuntimeError("Color object type not recognised.")

    def invoke(self):
        """
        Implements the defined action.
        :return: a Job object, describing the job implementing the action.
        """

        base="data_request?id=action"

        action = "SetColor"
        var = "newColorTarget"
        value = str(self.color)

        svc = "urn:micasaverde-com:serviceId:Color1"
        path = "%s&DeviceNum=%d&serviceId=%s&action=%s&%s=%s&output_format=json" \
               % (base, self.device.id, svc, action, var, value)

        status = self.device.vera.get(path)
        job = Job()

        job.id = int(status["u:SetColorResponse"]["JobID"])
        job.vera = self.device.vera
        return job

    @staticmethod
    def parse(vera, s):
        """
        Converts LUUP SetTarget values to a ColorAction object.

        :param s: Value from LUUP comms.
        """
        sa = ColorAction()

        sa.device = vera.get_device_by_id(s["device"])
        value = s["arguments"][0]["value"]

        if s["action"] == "SetColorRGB":
            cols = value.split(",")
            if len(cols) != 3:
                raise RuntimeError("Could not parse RGB: %s", value)
            cols = [ int(i) for i in cols ]
            sa.color = RGB(cols[0], cols[1], cols[2])

        elif s["action"] == "SetColor" and value[0] == "D":

            sa.color = Daylight(int(value[1:]))

        elif s["action"] == "SetColor" and value[0] == "W":

            sa.color = Warm(int(value[1:]))

        return sa

class SceneAction(Action):
    """
    Action which runs a scene
    """

    def __init__(self, vera=None, id=None):
        """
        Creates a RGAction object.
        :param device: Device object describing the device to apply
        :param value: value for color
        """
        self.vera = vera
        self.id = id

    def output(self):
        """
        Formats the value in a format suitable for LUUP comms.
        """
        return {
            "action": "RunScene",
            "arguments": [
                {
                    "name": "SceneNum", 
                    "value": self.id
                }
            ], 
            "service": "urn:micasaverde-com:serviceId:HomeAutomationGateway1"
        }

    def invoke(self):
        """
        Implements the defined action.
        :return: a Job object, describing the job implementing the action.
        """

        base="data_request?id=action"
        action = "RunScene"
        svc = "urn:micasaverde-com:serviceId:HomeAutomationGateway1"
        path = "%s&serviceId=%s&action=%s&SceneNum=%d&output_format=json" \
               % (base, svc, action, self.id)
        status = self.vera.get(path)

        if status["u:RunSceneResponse"]["OK"] != "OK":
            return False

        return True

    @staticmethod
    def parse(vera, s):
        """
        Converts LUUP SetTarget values to a RGBAction object.

        :param s: Value from LUUP comms.
        """
        sa = RGBAction()
        sa.vera = vera
        sa.value = s["arguments"][0]["value"]
        return sa

class Group(object):
    """
    A list of Action objects plus a delay time for when the actions are applied,
    """

    def __init__(self, delay=None, actions=None):
        """
        Creates an Group object

        :param delay: delay in seconds
        :param actions: sequence of Action objects
        """
        self.delay = delay
        self.actions = actions

        if self.actions == None: self.actions = []

    def output(self):
        """
        Formats the time value in a format suitable for LUUP comms.
        """
        acts = []
        for i in self.actions:
            acts.append(i.output())
        return {
            "delay": self.delay,
            "actions": acts
        }

    @staticmethod
    def parse(vera, s):
        """
        Converts LUUP group value to an Group object.

        :param s: Value from LUUP comms.
        """
        aset = Group()

        aset.delay = s.get("delay", 0)

        if "actions" in s:
            for i in s["actions"]:
                aset.actions.append(Action.parse(vera, i))

        return aset

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        return self.__dict__ == obj.__dict__ and type(self) == type(obj)

class SceneDefinition(object):

    def __init__(self, name=None, triggers=None, modes=None, timers=None,
                 actions=None, room=None, lua=None):

        self.name = name

        if triggers != None:
            self.triggers = triggers
        else:
            self.triggers = []
            
        self.modes = modes

        if timers != None:
            self.timers = timers
        else:
            self.timers = []

        if actions != None:
            self.actions = actions
        else:
            self.actions = []

        self.room = room

        self.lua = lua

    def output(self):
        """
        Formats the time value in a format suitable for LUUP comms.
        """

        triggers = []
        for i in self.triggers:
            triggers.append(i.output())

        timers = []
        for i in self.timers:
            timers.append(i.output())

        actions = []
        for i in self.actions:
            actions.append(i.output())

        val = {
            "name": self.name,
            "triggers": triggers,
            "triggers_operator": "OR", 
            "timers": timers,
            "groups": actions,
            "users": "", 
        }

        if self.modes != None:
            val["modeStatus"] = self.modes.output()

        if self.room != None:
            val["room"] = self.room.id

        if self.lua != None:
            val["lua"] = base64.b64encode(self.lua.encode("utf-8")).decode("utf-8")
            val["encoded_lua"] = 1

        return val

    @staticmethod
    def parse(vera, s):
        """
        Converts LUUP scene to a SceneDefinition object.

        :param s: Value from LUUP comms.
        """

        sd = SceneDefinition()
        
        sd.name = s["name"]

        if "triggers" in s:
            for i in s["triggers"]:
                sd.triggers.append(Trigger.parse(vera, i))

        if "timers" in s:
            for i in s["timers"]:
                sd.timers.append(Timer.parse(i))

        if "groups" in s:
            for i in s["groups"]:
                sd.actions.append(Group.parse(vera, i))

        if "room" in s:
            if s["room"] == 0:
                sd.room = None
            else:
                sd.room = vera.get_room_by_id(s["room"])

        if "modeStatus" in s:
            sd.modes = Modes.parse(vera, s["modeStatus"])

        if "lua" in s:
            sd.lua = base64.b64decode(s["lua"]).decode("utf-8")

        return sd

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        return self.__dict__ == obj.__dict__ and type(self) == type(obj)

class Modes(object):
    """
    Describes the set of modes for which a scene will be valid
    """
    
    def __init__(self, home=False, away=False, night=False, vacation=False):
        """
        Creates a Modes object
        :param home: True for scene to be valid in home mode
        :param away: True for scene to be valid in away mode
        :param night: True for scene to be valid in night mode
        :param vacation: True for scene to be valid in vacation mode
        """
        self.home, self.away, self.night = home, away, night
        self.vacation = vacation

    def output(self):
        """
        Formats the value in a format suitable for LUUP comms.
        """
        val = ""
        if self.home:
            val = "1"
        if self.away:
            if val != "": val = val + ","
            val = val + "2"
        if self.night:
            if val != "": val = val + ","
            val = val + "3"
        if self.vacation:
            if val != "": val = val + ","
            val = val + "4"
        return val

    @staticmethod
    def parse(vera, s):
        """
        Converts LUUP modeSet values to a Mode object.

        :param vera: A vera object.
        :param s: Value from LUUP comms.
        """
        x = s.split(",")
        y = {}
        for i in x:
            y[i] = True

        m = Modes()
        m.home = y.get(0, None)
        m.away = y.get(1, None)
        m.night = y.get(2, None)
        m.vacation = y.get(3, None)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        if obj == None: return False
        return self.__dict__ == obj.__dict__ and type(self) == type(obj)

class Device(object):
    """
    Describes a LUUP device
    """

    def __init__(self):
        """
        Creates a Device object
        """
        pass

    def get_variable(self, svc, var):
        """
        Queries the LUUP engine for the value of a variable.
        
        :param svc: LUUP service
        :param var: Variable name.
        """
        action = "variableget"
        path = "data_request?id=%s&DeviceNum=%d&serviceId=%s&Variable=%s" \
               % (action, self.id, svc, var)
        return self.vera.get(path)

    def get_switch(self):
        """
        Get the current state of a power switch device.  Returns a boolean
        value.
        """

        svc = "urn:upnp-org:serviceId:SwitchPower1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")
        
        status = self.get_variable(svc, "Status")
        return status == 1

    def get_rgb(self):
        """
        Get the current state of an RGB device.  Returns a string.
        """

        svc = "urn:upnp-org:serviceId:RGBController1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")

        # Strip off hash.
        return self.get_variable(svc, "Color")[1:]

    def get_color(self):
        """
        Get the current color of a device which supports color.
        Returns a dict mapping channel ID to color value (an int).
        """

        svc = "urn:micasaverde-com:serviceId:Color1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")

        val = self.get_variable(svc, "CurrentColor")

        channel_map = {
            0: 'W', 1: 'D', 2: 'R', 3: 'G', 4: 'B'
        }

        valmap = {}
        for part in val.split(","):
            k, v = part.split("=")
            if int(k) in channel_map:
                valmap[channel_map[int(k)]] = int(v)

        # Hard-coded logic.  In ZW098, Warm white over-rides Daylight white,
        # over-rides RGB.

        if "W" in valmap and valmap["W"] > 0:
            return Warm(valmap["W"])

        if "D" in valmap and valmap["D"] > 0:
            return Daylight(valmap["D"])

        return RGB(valmap["R"], valmap["G"], valmap["B"])

    def set_color(self, value):
        """
        Get the current color of a device which supports color.  
        Returns a string.
        """

        svc = "urn:micasaverde-com:serviceId:Color1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")

        # if isinstance(value, Warm):
        #     ColorAction(self, Daylight(0)).invoke()
        #     ColorAction(self, RGB(0, 0, 0)).invoke()
        # elif isinstance(value, Daylight):
        #     ColorAction(self, Warm(0)).invoke()
        #     ColorAction(self, RGB(0, 0, 0)).invoke()
        # elif isinstance(value, RGB):
        #     ColorAction(self, Warm(0)).invoke()
        #     ColorAction(self, Daylight(0)).invoke()

        # Get color channels, and produce an channel ID to number map.
        act = ColorAction(self, value)
        return act.invoke()

    def get_dimmer(self):
        """
        Get the current state of a dimmer device.  Returns an integer in
        the range 0-100.
        """

        svc = "urn:upnp-org:serviceId:Dimming1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")

        return self.get_variable(svc, "LoadLevelStatus")

    def get_temperature(self):
        """
        Get the current value of a temperature sensor device.  Returns a
        floating point value.  The temperature scale in use is dependent on 
        device configuration.
        """

        svc = "urn:upnp-org:serviceId:TemperatureSensor1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")

        return self.get_variable(svc, "CurrentTemperature")

    def get_humidity(self):
        """
        Get the current value of a humidity sensor device.  Returns a
        integer value representing % relative humidity.
        """

        svc = "urn:micasaverde-com:serviceId:HumiditySensor1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")

        return self.get_variable(svc, "CurrentLevel")
     
    def get_lux(self):
        """
        Get the current value of a light sensor device.  Returns a
        integer value representing % of lighting.
        """

        svc = "urn:micasaverde-com:serviceId:LightSensor1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")

        return self.get_variable(svc, "CurrentLevel")
      
    def get_kwh(self):
        """
        Get the current value of the energy meter in kwh.  Returns a
        integer value with current kilowatts being used.
        """

        svc = "urn:micasaverde-com:serviceId:EnergyMetering1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")

        return self.get_variable(svc, "KWH")
      
    def get_kwh_reading(self):
        """
        Get the current reading of the energy meter in kwh.  Returns a
        integer value with to date kilowatts being used.
        """

        svc = "urn:micasaverde-com:serviceId:EnergyMetering1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")

        return self.get_variable(svc, "KWHReading")
      
    def get_watt(self):
        """
        Get the current value of the energy meter in watts.  Returns a
        integer value with current wattage being used.
        """

        svc = "urn:micasaverde-com:serviceId:EnergyMetering1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")

        return self.get_variable(svc, "Watts")

    def get_setpoint(self):
        """
        Get the 'set point' of a thermostat device.  This is the temperature
        at which the device is configured to turn on heating.
        """
        svc = "urn:upnp-org:serviceId:TemperatureSetpoint1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")

        return self.get_variable(svc, "CurrentSetpoint")

    def get_heating(self):
        """
        Get the operating mode of a heating device.  Valid values are:
        Off, HeatOn.
        """

        svc = "urn:upnp-org:serviceId:HVAC_UserOperatingMode1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")
        
        return self.get_variable(svc, "ModeStatus")

    def get_battery(self):
        """
        Get the battery capacity of a battery-powered device.  Is a %
        value, 0-100.
        """

        svc = "urn:micasaverde-com:serviceId:HaDevice1"
        if not svc in self.services:
            raise RuntimeError("Device doesn't support the service")

        return self.get_variable(svc, "BatteryLevel")

    def set_switch(self, value):
        """
        Changes the setting of a switch device.

        :param value: new value, boolean
        """
        act = SwitchAction(self, value)
        return act.invoke()

    def set_rgb(self, value):
        """
        Changes the setting of an RGB device.

        :param value: new value, string in form #aabbccddee
        """
        act = RGBAction(self, value)
        return act.invoke()

    def set_dimmer(self, value):
        """
        Changes the setting of a dimmer device.

        :param value: new value, 0-100.
        """
        act = DimmerAction(self, value)
        return act.invoke()

    def set_setpoint(self, value):
        """
        Changes the set point of a thermostat device.

        :param value: new value, float.
        """
        act = SetpointAction(self, value)
        return act.invoke()

    def set_heating(self, value):
        """
        Changes the operating mode of a heating device.

        :param value: new value, string, valid values are: Off HeatOn.
        """
        act = HeatingAction(self, value)
        return act.invoke()

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        return self.__dict__ == obj.__dict__ and type(self) == type(obj)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        return self.__dict__ == obj.__dict__ and type(self) == type(obj)

class Scene(object):
    """
    Represents a scene, once it is configured into the LUUP engine.
    """
    def __init__(self):
        """
        Creates a Scene object.
        """
        pass

    def delete(self):
        """
        Calls the LUUP engine to delete this scene.
        """
        self.vera.delete_scene(self)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        return self.__dict__ == obj.__dict__ and type(self) == type(obj)

    def run(self):
        self.vera.run_scene(self.id)
        
class Room(object):
    """
    Represents a room, configured into the LUUP engine.
    """

    def __init__(self):
        pass

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        if type(self) != type(obj): return False
        return self.__dict__ == obj.__dict__

class Vera(object):
    """
    Vera represents a connection to a Vera device's LUUP engine.
    """
    def __init__(self):
        """
        Creates a new Vera object.
        """
        self.update_state()

    def update_state(self):
        """
        Queries the LUUP engine for user_data state, and updates the local
        copy.
        """
        ud = self.get('data_request?id=user_data&output_format=json')
        self.user_data = ud

        self.rooms = {}
        for i in self.user_data["rooms"]:
            s = Room()
            s.vera = self
            s.id = int(i["id"])
            s.name = i["name"]
            self.rooms[s.id] = s

        self.devices = {}
        for i in self.user_data["devices"]:

            d = Device()
            d.vera = self
            d.id = int(i["id"])
            d.name = i["name"]

            if "manufactuerer" in i:
                d.manufacturer = i["manufacturer"]
            else:
                d.manufacturer = None

            if "model" in i:
                d.model = i["model"]
            else:
                d.model = None

            d.services = set()
            for st in i["states"]:
                d.services.add(st["service"])

            d.device_type = i["device_type"]

            if "device_file" in i:
                d.device_file = i["device_file"]
                
            if "device_json" in i:
                d.device_json = i["device_json"]

            if "invisible" in i and int(i["invisible"]) > 0:
                d.invisible = True
            else:
                d.invisible = False
            
            if "room" in i and int(i["room"]) in self.rooms:
                d.room = self.rooms[int(i["room"])]
            else:
                d.room = None
            self.devices[d.id] = d

        self.scenes = {}

        for i in self.user_data["scenes"]:

            s = Scene()
            
            s.vera = self
            s.id = int(i["id"])
            s.name = i["name"]
            if 'room' in i and int(i["room"]) in self.rooms:
                s.room = self.rooms[int(i["room"])]
            else:
                s.room = None

            s.definition = SceneDefinition.parse(self, i)
            
            self.scenes[s.id] = s

    def get_room_by_id(self, id):
        """
        Return a Room object if one exists matching the provided ID.
        :param id: Room ID, an integer
        :return: A Room object
        """
        if not isinstance(id, int):
            id = int(id)
        if id in self.rooms:
            return self.rooms[id]
        raise RuntimeError("Room not known")

    def get_room(self, name):
        """
        Return a Room object if one exists with the provided room name.
        :param name: Room name.
        :return: A Room object
        """
        for i in self.rooms:
            if self.rooms[i].name == name:
                return self.rooms[i]
        raise RuntimeError("Room '%s' not known" % name)

    def get_device(self, name, room=None):
        """
        Return a Device object if one exists with the provided device name.
        Optionally, a room object can be specified to restrict the search for
        the device to that room.
        :param name: Device name.
        :param room: Optional Rooom object.
        :return: A Device object
        """
        for i in self.devices:
            if self.devices[i].name == name:
                if room == None or self.devices[i].room == room:
                    return self.devices[i]
        raise RuntimeError("Device '%s' not known" % name)

    def get_device_by_id(self, id):
        """
        Return a Device object if one exists matching the provided ID.
        :param id: Device ID, an integer
        :return: A Device object
        """
        if not isinstance(id, int):
            id = int(id)
        for i in self.devices:
            if self.devices[i].id == id:
                return self.devices[i]
        raise RuntimeError("Device not found")

    def get_devices(self):
        """
        Return a sequence of devices.
        :return: A sequence of Device objects.
        """
        devices = []
        for i in self.devices:
            devices.append(self.devices[i])

        return devices

    def get_scenes(self):
        """
        Returns a list of scenes.
        :return: A sequence of Scene objects.
        """
        scenes = []
        for i in self.scenes:
            scenes.append(self.scenes[i])

        return scenes

    def get_rooms(self):
        """
        Returns a list of rooms.
        :return: A sequence of Room objects.
        """
        rooms = []
        for i in self.rooms:
            rooms.append(self.rooms[i])

        return rooms

    def get(self, path):
        """
        Performs an HTTP/S 'GET' for a LUUP resource, which is returned.

        :param path: Relative path for the resource e.g. data_request?id=alive
        :return: The resource.  If the underlying resource is JSON, this is
        converted to Python dict.
        """
        raise RuntimeError("Not implemented")

    def get_user_data(self):
        """
        Returns the user_data.  Doesn't fetch, this is a local copy.
        :return: user_data as a Python dict.
        """
        return self.user_data
  
    def get_sdata(self):
        """
        Fetches the sdata from the LUUP engine.

        :return: sdata as a dict.
        """
        payload = self.get('data_request?id=sdata&output_format=json')
        return payload

    def get_file(self, path):
        """
        Fetches a file from the Vera device.
        :param path: filename.
        :return: file contents
        """
        file = self.get('data_request?id=file&parameters=%s' % path)
        return file
  
    def get_status(self):
        """
        Gets Vera status.
        :return: status value.
        """
        payload = self.get('data_request?id=status&output_format=json')
        return payload
  
    def get_scene(self, id):
        """
        Fetches a scene from the LUUP device.  You probably want to use
        get_scenes, to access Scene objects.
        :param id: scene ID.
        :return: scene as Python dict, not a Scene object.
        """
        if not isinstance(id, int):
            id = int(id)
        payload = self.get('data_request?id=scene&action=list&scene=%d&output_format=json' % id)
        return payload

    def delete_scene(self, s):
        """
        Deletes a Scene from Vera.
        :param s: A Scene object
        """
        return self.get('data_request?id=scene&action=delete&scene=%s' % s.id)
  
    def create_scene(self, s):
        """
        Creates a Scene object from a SceneDefinition object.

        :param s: SceneDefinition object.
        """
        s = json.dumps(s.output())

        # URL-encoding.  Vera not happy with Python's standard
        # URL-encoding.
        s = Vera.urlencode(s)
        
        payload = self.get('data_request?id=scene&action=create&json=%s' % s)
        return payload

    def run_scene(self, id):
        """
        Run a scene by ID.

        :param id: Scene number.
        """
        act = SceneAction(self, id)
        return act.invoke()

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        return self.__dict__ == obj.__dict__ and type(self) == type(obj)

    @staticmethod
    def urlencode(s):
        # URL-encoding.  Vera not happy with Python's standard
        # URL-encoding.
        s = s.replace("%", "%25")
        s = s.replace(":", "%3a")
        s = s.replace("+", "%2b")
        s = s.replace("&", "%26")
        s = s.replace("{", "%7b")
        s = s.replace("}", "%7d")
        s = s.replace("'", "%27")
        s = s.replace('"', "%22")
        s = s.replace("?", "%3f")
        s = s.replace(" ", "%20")
        s = s.replace("/", "%2f")
        return s
        
    def get_weather(self):
        """
        Gets the weather status for the current location.
        :returns: a dict containing elements: code, weather, temperature.
        Code is a weather code (origin unknown?) weather is a string
        containing a token.  The weather token is reverse-engineered, accuracy
        unknown.
        """

        city = self.user_data["weatherSettings"]["weatherCity"]
        country = self.user_data["weatherSettings"]["weatherCountry"]

        host = "weather.mios.com"
        temp_scale = "C"
        url = "http://%s/?tempFormat=%s&cityWeather=%s&countryWeather=%s" % \
              (host, temp_scale, Vera.urlencode(city), Vera.urlencode(country))

        resp = {}

        weather = self.proxy_get(url)

        if "code" in weather:
            resp["code"] = weather["code"]
            if weather["code"] in weather_types:
                resp["weather"] = weather_types[weather["code"]]

        resp["temperature"] = weather["temp"]

        return resp

    def all_switches(self, value):
        """
        Implement a state change to all switches.
        :param value: The value to apply to all switches, a boolean.
        :return: a Job object, describing the job implementing the action.
        """

        if value:
            value = 1
        else:
            value = 0

        base="data_request?id=action"
        action = "SetTarget"
        svc = "urn:upnp-org:serviceId:SwitchPower1"
        path = "%s&Category=%d&serviceId=%s&action=%s&newTargetValue=%d&output_format=json" \
               % (base, 3, svc, action, value)
        status = self.get(path)

        job = Job()
        job.id = int(status["u:SetTargetResponse"]["JobID"])
        job.vera = self
        return job

    def all_dimmers(self, value):
        """
        Implement a state change to all dimmer devices.
        :param value: The value to apply to all devices, an integer 0-100.
        :return: a Job object, describing the job implementing the action.
        """

        base="data_request?id=action"
        action = "SetLoadLevelTarget"
        svc = "urn:upnp-org:serviceId:Dimming1"
        path = "%s&Category=%d&serviceId=%s&action=%s&newTargetValue=%d&output_format=json" \
               % (base, 2, svc, action, value)
        status = self.get(path)

        job = Job()
        job.id = int(status["u:SetTargetResponse"]["JobID"])
        job.vera = self
        return job

    def all_lights(self, value):
        """
        Implement a state change to all light devices.
        :param value: The value to apply to all switches, a value 0-100.
        :return: a Job object, describing the job implementing the action.
        """

        if value:
            value = 1
        else:
            value = 0

        base="data_request?id=action"
        action = "SetTarget"
        svc = "urn:upnp-org:serviceId:SwitchPower1"
        path = "%s&Category=%d&serviceId=%s&action=%s&newTargetValue=%d&output_format=json" \
               % (base, 999, svc, action, value)
        status = self.get(path)

        job = Job()
        job.id = int(status["u:SetTargetResponse"]["JobID"])
        job.vera = self
        return job

    def all_heating(self, value):
        """
        Implement a state change to all heating devices.
        :param value: The value to apply to all switches, a string.
        :return: a Job object, describing the job implementing the action.
        """

        base="data_request?id=action"
        action = "SetModeTarget"
        svc = "urn:upnp-org:serviceId:HVAC_UserOperatingMode1"
        path = "%s&Category=%d&serviceId=%s&action=%s&NewModeTarget=%s&output_format=json" \
               % (base, 5, svc, action, value)
        status = self.get(path)

        job = Job()
        job.id = int(status["u:SetModeTargetResponse"]["JobID"])
        job.vera = self
        return job

class VeraLocal(Vera):
    """
    Represents a connection to a local Vera device.
    """

    def __init__(self, host, port = 3480):
        """
        Connects to a local Vera device on the local network.
        :param host: string containing hostname or IP address.
        :param port: port number.
        """
        self.host = host
        self.port = port
        Vera.__init__(self)

    def get(self, path):
        """
        Performs an HTTP/S 'GET' for a LUUP resource, which is returned.

        :param path: Relative path for the resource e.g. data_request?id=alive
        :return: The resource.  If the underlying resource is JSON, this is
        converted to Python dict.
        """
        base = 'http://%s:%d' % (self.host, self.port)
        url = '%s/%s' % (base, path)

        req = requests.get(url)
        payload = req.text

        try:
            # If JSON, decode else move on.
            payload = json.loads(payload)
        except:
            pass

        return payload

    def proxy_get(self, url):

        url = Vera.urlencode(url)

        url = "http://%s/cgi-bin/cmh/proxy.sh?url=%s" % \
              (self.host, url)

        response = requests.get(url)

        try: 
            return response.json()
        except:
            pass

        return response.text

class VeraRemote(Vera):

    def get_session_token(self, server):
        """
        Get a session token for subsequent operations on a server.  You
        shouldn't need to call this.
        :param server: the server.
        :return: session token string.
        """
        headers = {"MMSAuth": self.auth_token, "MMSAuthSig": self.auth_sig}
        url = "https://%s/info/session/token" % server
        session_token = self.session.get(url, headers=headers).text

        return session_token

    def __init__(self, user, password, device):
        """
        Connects to a remote Vera device through the relay servers.
        :param user: username.
        :param password: password.
        :param device: device ID
        """
        self.user = user
        self.password = password
        self.device = device
        self.session = requests.session()

        # Hard-coded auth seed
        seed = "oZ7QE6LcLJp6fiWzdqZc"

        # Get auth tokens
        sha1p = user.lower() + password + seed
        sha1p = sha1p.encode("utf-8")
        sha1p = hashlib.sha1(sha1p)
        sha1p = sha1p.hexdigest()

        auth_server = "vera-us-oem-autha11.mios.com"

        url = "https://%s/autha/auth/username/%s?SHA1Password=%s&PK_Oem=1" % \
              (auth_server, user.lower(), sha1p)

        response = self.session.get(url).json()

        self.server_account = response["Server_Account"]
        self.auth_token = response["Identity"]
        self.auth_sig = response["IdentitySignature"]

        # Get account number
        account_info = json.loads(base64.b64decode(self.auth_token))
        pk_account = account_info["PK_Account"]
        sys.stderr.write("Account number: %s\n" % pk_account)

        # Get session token for server account
        session_token = self.get_session_token(self.server_account)

        # Get devices
        headers = { "MMSSession": session_token }
        url = "https://%s/account/account/account/%s/devices" % \
              (self.server_account, str(pk_account))
        devices = self.session.get(url, headers=headers).json()

        # Work out server device
        server_device = None
        for i in devices["Devices"]:
            if i["PK_Device"] == device:
                server_device = i["Server_Device"]
        if server_device == None:
            raise RuntimeError("Device %s not known." % device)
                
        sys.stderr.write("Server device: %s\n" % server_device)

        # Get session token on server_device
        session_token = self.get_session_token(server_device)

        # Get server_relay
        headers = { "MMSSession": session_token }

        url = "https://" + server_device + "/device/device/device/" + \
              str(device)

        relay_info = self.session.get(url, headers=headers).json()

        self.relay = relay_info["Server_Relay"]

        sys.stderr.write("Server relay: %s\n" % self.relay)

        # Get session token on server_relay
        self.session_token = self.get_session_token(self.relay)

        Vera.__init__(self)

        sys.stderr.write("Connected to remote device.\n")

    def get(self, path):
        """
        Performs an HTTP/S 'GET' for a LUUP resource, which is returned.

        :param path: Relative path for the resource e.g. data_request?id=alive
        :return: The resource.  If the underlying resource is JSON, this is
        converted to Python dict.
        """

        headers = { "MMSSession": self.session_token }

        url = "https://%s/relay/relay/relay/device/%s/port_3480/%s" % \
              (self.relay, str(self.device), path)

        response = requests.get(url, headers=headers)

        try: 
            return response.json()
        except:
            pass

        return response.text

    def proxy_get(self, url):

        url = Vera.urlencode(url)

        headers = { "MMSSession": self.session_token }

        url = "https://%s/relay/relay/proxy?url=%s" % (self.relay, url)

        response = requests.get(url, headers=headers)

        try: 
            return response.json()
        except:
            pass

        return response.text

#http://control/cgi-bin/cmh/proxy.sh?url=http%3A%2F%2Fweather.mios.com%2F%3FtempFormat%3DC%26cityWeather%3DCheltenham%2520England%26countryWeather%3DUnited%2520Kingdom

def connect(config="LUUP-AUTH.json"):
    """
    Gets Vera connection information from a file, and connects to a Vera.
    :param config: filename
    :return: a Vera object on successful connection.
    """
    config = json.loads(open(config, "r").read())

    if "local" in config:
        return VeraLocal(config["local"]["address"])
    else:
        user = config["remote"]["user"]
        password = config["remote"]["password"]
        device = config["remote"]["device"]
        return VeraRemote(user, password, device)

