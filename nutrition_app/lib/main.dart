import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/semantics.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Wegmans Test App',
      theme: ThemeData(
        primarySwatch: Colors.red,
      ),
      home: FutureBuilder<bool>(
        future: checkLoginValue(),
        builder: (BuildContext context, AsyncSnapshot<bool> snapshot){
          print(snapshot.data);
          if (snapshot.data == true) {
            return HomePage();
          } else {
            return LandingPage();
          }
        }
      )
    );
  }
}

/*
 * HOME PAGE CODE
 * BELOW THIS COMMENT
 */

class HomePage extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: getThemeData(),
      home: Scaffold(
        appBar: AppBar(title: const Text("Dhaval")),
      ),
    );
  }
}

/*
 * LANDING PAGE CODE
 * BELOW THIS COMMENT
 */ 

class LandingPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
        title: Text("Flutter Radio Button Group Example"),
        ),
        body: SafeArea(
          child : Center(
          child : RadioGroup(),
          )
        )
      ),
    );
  }
}

class RadioGroup extends StatefulWidget {
  @override
  RadioGroupWidget createState() => RadioGroupWidget();
}

class GenderList {
  String name;
  int index;
  GenderList({this.name, this.index});
}

class RadioGroupWidget extends State {

  // Default Radio Button Item
  String radioItem = 'Male';

  // Group Value for Radio Button.
  int id = 1;

  //TextField Storage
  TextEditingController weightController = new TextEditingController();

  List<GenderList> gList = [
    GenderList(
      index: 1,
      name: "Male",
    ),
    GenderList(
      index: 2,
      name: "Female",
    ),
    GenderList(
      index: 3,
      name: "Other",
    ),
  ];

  Widget build(BuildContext context) {
    return Column(
        children: <Widget>[
          Padding(
            padding : EdgeInsets.all(14.0),
            child: Text(
              'Please Select your Gender:',
              style: TextStyle(fontSize: 23)
              )
          ),
          Container(
            child: Container(
              height: 250.0,
              child: Column(
                children: 
                  gList.map((data) => RadioListTile(
                    title: Text("${data.name}"),
                    groupValue: id,
                    value: data.index,
                    onChanged: (val) {
                      setState(() {
                        radioItem = data.name;
                        id = data.index;
                      });
                    },
                  )).toList(),
              ),
            ),
          ),
          Text(
            'Please Enter your Weight:',
            style: TextStyle(fontSize: 23)
          ),
          Padding(
            padding : EdgeInsets.all(14.0),
          ),
          Container(
            width: 100,
            child: TextField(
              controller: weightController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                hintText: 'pounds'
              )
            ),
          ),
          Padding(
            padding: EdgeInsets.all(100.0),
          ),
          ButtonTheme(
            minWidth: 200.0,
            height: 70.0,
            child: RaisedButton(
              textColor: Colors.white,
              color: Colors.blue,
              onPressed: () {
                if(!isNumeric(weightController.text)) {
                  _ackAlert(context);
                } else {
                  setHumanSex(radioItem);
                  setHumanWeight(double.parse(weightController.text));
                  setLoginValue();
                  navigateToHomePage(context);
                }
              },
              child: const Text(
                'Submit',
                style: TextStyle(fontSize: 20)
              )
            )
          )
        ],
    );
  }
}

/**
 * SUPPORTING FUNCTIONS
 * BELOW THIS COMMENT
 */

//Checks if a string is numeric
bool isNumeric(String s) {
  if(s == null) {
    return false;
  }
  return double.tryParse(s) != null;
}

Future<void> _ackAlert(BuildContext context) {
  return showDialog<void>(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text('Error'),
        content: const Text('Please enter a correct weight value'),
        actions: <Widget>[
          FlatButton(
            child: Text('OK'),
            onPressed: () {
              Navigator.of(context).pop();
            })
        ],
      );
    }
  );
}

//Navigate to HomePage
Future navigateToHomePage(context) async {
  Navigator.push(context,
    MaterialPageRoute(builder: (context) => HomePage()));
}

//Get Common Theme Data
ThemeData getThemeData() {
  return ThemeData(
    primarySwatch: Colors.red,
  );
}

//Check if user has logged in before
Future<bool> checkLoginValue () async {
  SharedPreferences loginCheck = await SharedPreferences.getInstance();
  return loginCheck.getBool("login");
}

//Set value that user has logged in
setLoginValue() async {
  SharedPreferences loginCheck = await SharedPreferences.getInstance();
  await loginCheck.setBool("login", true);
}

//Set a human's weight
setHumanWeight(double weight) async {
  SharedPreferences pref = await SharedPreferences.getInstance();
  await pref.setDouble("wieght", weight);
}

//Set a human's sex
setHumanSex(String string) async {
  SharedPreferences pref = await SharedPreferences.getInstance();
  await pref.setString("sex", string);
}