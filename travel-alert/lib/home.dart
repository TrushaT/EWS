import 'package:flutter/material.dart';
import 'calendarpage.dart';
import 'package:http/http.dart' as http;
import 'http_service.dart';
import 'dart:async';
import 'dart:convert';

Future<Weather> sendlocation(List<String> locations) async {

  final response = await http.post(
    Uri.https('url', 'locations'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, List<String>>{
      'location': locations,
    }),
  );

  if (response.statusCode == 201) {
    return Weather.fromJson(jsonDecode(response.body));
  } else {
    throw Exception('Failed to send location.');
  }
}

class Weather {
  final int id;
  final String update;

  Weather({this.id, this.update});

  factory Weather.fromJson(Map<String, dynamic> json) {
    return Weather(
      id: json['id'],
      update: json['update'],
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  Widget _buildRow(int index) {
    return ListTile(
      leading: CircleAvatar(
        child: Text('$index'),
      ),
      title: Text(locations[index]),
    );
  }

   Future<Weather> _futureupdate;

  getevents() async {
    await retrieveCalendars();
  }


@override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Weather Updates',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text('Send data'),
        ),
        body: Container(
          alignment: Alignment.center,
          padding: const EdgeInsets.all(8.0),
          child: (_futureupdate == null)
              ? Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    
                    ElevatedButton(
                      child: Text('send data'),
                      onPressed: () {
                        setState(() {
                          _futureupdate = sendlocation(locations);
                        });
                      },
                    ),
                  ],
                )
              : FutureBuilder<Weather>(
                  future: _futureupdate,
                  builder: (context, snapshot) {
                    if (snapshot.hasData) {
                      return Text(snapshot.data.update);
                    } else if (snapshot.hasError) {
                      return Text("${snapshot.error}");
                    }

                    return CircularProgressIndicator();
                  },
                ),
        ),
      ),
    );
  }
}
