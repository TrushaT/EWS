import 'package:flutter/material.dart';
import 'package:device_calendar/device_calendar.dart';
import 'dart:collection';
import 'dart:io';

List<Calendar> calendars;
List<String> CalendarNames = [];
List<String> locations = [];

List<UnmodifiableListView<Event>> calEventlist = [];

final startDate = DateTime.now().add(Duration(days: -1));
final endDate = DateTime.now().add(Duration(days: 2));

DeviceCalendarPlugin _deviceCalendarPlugin = new DeviceCalendarPlugin();

retrieveCalendars() async {
  //Retrieve user's calendars from mobile device
  //Request permissions first if they haven't been granted
  try {
    var permissionsGranted = await _deviceCalendarPlugin.hasPermissions();

    if (permissionsGranted.isSuccess && !permissionsGranted.data) {
      permissionsGranted = await _deviceCalendarPlugin.requestPermissions();

      if (!permissionsGranted.isSuccess || !permissionsGranted.data) {
        return;
      }
    }

    final calendarsResult = await _deviceCalendarPlugin.retrieveCalendars();
    calendars = calendarsResult?.data;
    print(calendars);

    for (int c = 0; c < calendars.length; c++) {
      CalendarNames.add(calendars[c].name);
      final calEvents = await _deviceCalendarPlugin.retrieveEvents(
          calendars[c].id,
          RetrieveEventsParams(startDate: startDate, endDate: endDate));

      if (calEvents.data != null) {
        calEventlist.add(calEvents.data);
      }
    }

    for (int c = 0; c < calEventlist.length; c++) {
      for (int i = 0; i < calEventlist[c].length; i++) {
        if (calEventlist[c][i].location.isNotEmpty) {
          locations.add(calEventlist[c][i].location);
        }
      }
    }
    print(locations);
    print(calEventlist);
    print(CalendarNames);
  } catch (e) {
    print(e);
  }
}
