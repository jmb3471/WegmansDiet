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

class ShoppingListItem extends State<ShoppingList>{
  final _font = const TextStyle(fontSize: 18.0);
  bool isedit = false;
  String titleVal = " Your Grocery List";
  var toRemove = new Set();
  var _items = ['1', '2', '3', '5'];

  Widget _buildRow(String str){
    bool inRemove = toRemove.contains(str);
    return ListTile(
      title: Text(
        str,
        style: _font,
      ),
      trailing: Icon(
        (isedit && inRemove) ? Icons.remove_circle : Icons.remove_circle,
        color: isedit ? (inRemove ? Colors.red : null) : Colors.white,
      ),
      onTap: (){
        if (isedit){
          setState(() {
            if(inRemove){
              toRemove.remove(str);
            } else {
              toRemove.add(str);
            }
          });
        }
      },
    );
  }

  Widget _buildList(){
    return ListView.builder(padding: const EdgeInsets.all(16.0),
      
      itemCount: 2 * _items.length,
      itemBuilder: (context, i) {
        if (i.isOdd) return Divider();

        final index = i ~/ 2;
        return _buildRow(_items[index]);
      });
  }

  void removeItems(){
    int i = 0;
    while (i < _items.length){
      if (toRemove.contains(_items[i])){
        toRemove.remove(_items[i]);
        _items.remove(_items[i]);
      } else {
        i++;
      }
    }
  }

  void convertMode(){
    setState(() {
      if (isedit) {
        titleVal = ' Your Grocery List';
        removeItems();
      } else {
        titleVal = ' Remove Items';
      }
      isedit = !isedit;
    });
  }
  
  @override
  Widget build(BuildContext context){
    return Scaffold(
    appBar: AppBar(
      title: Text(titleVal),
      actions: <Widget>[      // Add 3 lines from here...
          IconButton(icon: Icon(Icons.create), onPressed: convertMode),
        ],  
      ),
    body: _buildList(),
    );
  }
}

class ShoppingList extends StatefulWidget{

  ShoppingListItem createState() => ShoppingListItem();
  
}

/*
 * HOME PAGE CODE
 * BELOW THIS COMMENT
 */

class HomePage extends StatelessWidget{
 @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: ' Your Grocery List',
      home: ShoppingList(),
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
        title: Text(" Details"),
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
              height: 170.0,
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
            padding: EdgeInsets.all(40.0),
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

/*
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
  await pref.setDouble("weight", weight);
}

//Set a human's sex
setHumanSex(String string) async {
  SharedPreferences pref = await SharedPreferences.getInstance();
  await pref.setString("sex", string);
}

_makePostRequest() async {
  // set up POST request arguments
  String url = 'http://127.0.0.1:5000';
  Map<String, String> headers = {"Content-type": "application/json"};
  String json = '{"title": "Hello", "body": "body text", "userId": 1}';
  // make POST request
  Response response = await post(url, headers: headers, body: json);
  // check the status code for the result
  int statusCode = response.statusCode;