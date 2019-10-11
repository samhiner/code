//In the URL https://docs.google.com/spreadsheets/d/HELLO/edit#gid=0, SHEET_ID would be HELLO
SHEET_ID = '1O3Q8RU6WIOGxrtLK8Tq32zFeptvDaVuhwqESkTacKFU';

//this will be where the collected data is stored and what is handed back to the website
var output = {};

function doGet() {
  //open spreadsheet
  var spreadsheet = SpreadsheetApp.openById(SHEET_ID);
  var sheet = spreadsheet.getSheets()[0];
  var data = sheet.getDataRange().getValues();
  
  //add roles to output
  var x = 2;
  while (data[x][0] != '') {
    addData(data[0][0], data[x][0], data[x][1]);
    x++;
  }
  
  //add sponsored bills to output
  x = 2;
  while (data[x][3] != '') {
    addData(data[0][3], data[x][3], data[x][4], data[x][5], data[x][6]);
    x++;
  }
  
  //add votes to output
  x = 2;
  while (data[x][8] != '') {
    addData(data[0][8], data[x][8], data[x][9], data[x][10], data[x][11]);
    x++;
  }
  
  //add committees to output
  x = 2;
  while (data[x][13] != '') {
    addData(data[0][13], data[x][13], data[x][14]);
    x++;
  }
  
  Logger.log(output)
  return ContentService.createTextOutput("addStudentData('" + JSON.stringify(output) + "');").setMimeType(ContentService.MimeType.JAVASCRIPT);
}

//opt_misc should only have a value if opt_link has a value
function addData(type, person, description, opt_link, opt_misc) {
  if (output[person] == undefined) {
    output[person] = {};
  }
  
  if (output[person][type] == undefined) {
    output[person][type] = [];
  }
  
  if (opt_link == undefined) {
    output[person][type].push(description);
  } else if (opt_misc == undefined) {
    output[person][type].push([description, opt_link]);
  } else {
    output[person][type].push([description, opt_link, opt_misc]);
  }
}