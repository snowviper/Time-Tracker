var timer = document.getElementById("total-time");
var timerHoursStr = document.getElementById("activityHoursStr").textContent;
var currentTime = document.getElementById("currentTime");
var startBTN = document.getElementById("startBTN");
var stopBTN = document.getElementById("stopBTN");
var editBTN = document.getElementById("editBTN");
var insertBTN = document.getElementById("insertBTN");

var title = document.getElementById("title");
var levelDiv = document.getElementById("levelDiv");
var insertDiv = document.getElementById("insertDiv");

var activity_title = document.getElementById("activity-title");
var total_time = document.getElementById("total-time");
var currentTime = document.getElementById("currentTime");
var textItemColor = document.getElementsByClassName("textItemColor");



// create boolean var to prevent multiple edit presses from altering title text
var showTitleInput = true;
//hide delete BTN on page refresh




var totalTimeKeeper = new Stopwatch(timer, timerHoursStr);
var currentTimeKeeper = new Stopwatch(currentTime, "0");


startBTN.addEventListener("click", function(){
    if (!totalTimeKeeper.isOn){
        startBTN.innerHTML = '<span class="glyphicon glyphicon-pause"></span>';
        startBTN.style.backgroundColor = "DarkRed";
        startBTN.style.borderColor = "crimson";
        startBTN.style.color = "RGB(243, 23, 45)";


        totalTimeKeeper.start();
        currentTimeKeeper.start();

    }
    else if(totalTimeKeeper.isOn){
        startBTN.innerHTML = '<span class="glyphicon glyphicon-play"></span>';
        startBTN.style.backgroundColor = "rgb(4, 95, 65)";
        startBTN.style.borderColor = "lime";
        startBTN.style.color = "lime";




        totalTimeKeeper.stop();
        currentTimeKeeper.stop();
        loadXMLDoc();
    }
});

stopBTN.addEventListener("click", function(){
    if (totalTimeKeeper.isOn){
        totalTimeKeeper.stop();
        currentTimeKeeper.stop();
        loadXMLDoc();
    }
    
});

editBTN.addEventListener("click", function(){


    //get h1 text
    var activityTitle = document.getElementById("activity-title");

    //get insert form
    var insertForm = document.getElementById("insertForm");


    //store h1 title for use
    var activityTitleTxt = activityTitle.innerHTML;

    //get activity id in string form to send to function
    var activityID = document.getElementById("activityID");
    var activityIDInt = activityID.textContent;
    var activityIDString = activityIDInt.toString();

    //get List ID from activityID since activityID will never change 
    var activityList = document.getElementById(activityIDString);

    saveHandler = function(){
        activityTitle.style.color = "aquamarine";
        //get new title string from user
        var activityTitleInput = document.getElementsByName("activity-title")[0];

        //change string value in side bar
        activityList.innerHTML = activityTitleInput.value;

        var ajaxTitle = activityTitleInput.value + "$$TEXT$$" + activityIDString;
        saveActivityTitleAjax(ajaxTitle);

        //changes h1 title
        activityTitle.innerHTML = activityTitleInput.value;



        showTitleInput = true;
    }

    if (showTitleInput){
        activityTitle.style.color = "black";
        activityTitle.innerHTML = '<input type="text" name="activity-title" placeholder="activityTitle" value="'+ activityTitle.innerHTML +'"/>'
        + '<button type="button" class="btn-primary" onclick="saveHandler()">SAVE</button>';
        showTitleInput = false;

    }
    else{

    }
});

