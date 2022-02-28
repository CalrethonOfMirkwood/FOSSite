# Create Task - Linux Quiz 

## 1. Code
### HTML
```
<!DOCTYPE html>
{% extends "layouts/layout.html" .%}

{% block content .%}

<body>
    <!--Page Intro-->
    <h1 class="display-3 text-center" >Linux Proficiency Quiz</h1>
    <h3 class="lead text-center">This is a quiz that will determine your aptitude with Linux. Answer all 5 questions to the best of your ability and then press the submit button. After that, your total score will be given down below, and should you choose to receive a complex review by pressing the complex review button, you will receive specific scores based on your ability to complete questions about linux commands in specific, and general knowledge about linux</h3>

    <br>

    <!--Scoring Area-->
    <div class="container text-center">
        <div class="row">
            <div class="col">
                Total Score
            </div>
            <div class="col">
                General Linux Proficiency
            </div>
            <div class="col">
                Linux Terminal Command Proficiency
            </div>
        </div>
        <div class="row">
            <div class="col" id="total_scr"></div>
            <div class="col" id="genProf_scr"></div>
            <div class="col" id="code_scr"></div>
        </div>
    </div>

    <br>
    <br>

    <!--Form input for each question-->
    <form class="text-center">
        <h3 id="Q0"></h3>
        <input type = "text" id="A0">
        <h5 id="I0"></h5>

        <br>

        <h3 id="Q1"></h3>
        <input type = "text" id="A1">
        <h5 id="I1"></h5>

        <br>

        <h3 id="Q2"></h3>
        <input type = "text" id="A2">
        <h5 id="I2"></h5>

        <br>

        <h3 id="Q3"></h3>
        <input type = "text" id="A3">
        <h5 id="I3"></h5>

        <br>


        <input type = "button" onclick="CheckAns('simple')" value="Simple Review!">
        <input type = "button" onclick="CheckAns('complex')" value="Complex Review!">
        <br>
    </form>
</body>

<!--JS for randomizing+selecting questions-->
<script src={{  url_for("krish.static", filename="Fquiz_q.js", version='147') }}></script>
<!--JS for checking user answers-->
<script src={{  url_for("krish.static", filename="Fquiz_a.js", version='149') }}></script>

{% endblock %}
```

### Javascript for question shuffle 
```
// Randomizer - Created by Mohamad Hamouday 2018
function Pick_Random_Value(IN_Array)
{
    if(IN_Array != undefined && IN_Array.length > 0)
    {
        var Copy_IN_Array = JSON.parse(JSON.stringify(IN_Array));
        if((typeof window.Last_Pick_Random_Index !== 'undefined') && (window.Last_Pick_Random_Index !== false))
        {
            if(Copy_IN_Array[Last_Pick_Random_Index] != undefined)
            {
                Copy_IN_Array.splice(Last_Pick_Random_Index,1);
            }
        }

        var Return_Value = false;

        if(Copy_IN_Array.length > 0)
        {
            var Random_Key = Math.floor(Math.random() * Copy_IN_Array.length);
            Return_Value = Copy_IN_Array[Random_Key];
        }
        else
        {
            Return_Value = IN_Array[Last_Pick_Random_Index];
        }

        window.Last_Pick_Random_Index = IN_Array.indexOf(Return_Value);
        if(window.Last_Pick_Random_Index === -1)
        {
            for (var i = 0; i < IN_Array.length; i++)
            {
                if (JSON.stringify(IN_Array[i]) === JSON.stringify(Return_Value))
                {
                    window.Last_Pick_Random_Index = i;
                    break;
                }
            }
        }


        return Return_Value;
    }
    else
    {
        return false;
    }
}

// Main Function
var questions = {
    "What is the most universal command to access root privilages?": ["sudo","CODE"],
    "What does FOSS stand for?" : ["Free and Open Source Software","GENPROF"],
    "Linux is a(n)..." : ["kernel","GENPROF"],
    "What is the name of the place that RMS belongs?" : ["GNU","CODE"],
    "Which of the following characters can combine several commands?" : ["pipe - |","CODE"],
    "Can Linux can run on every computer?" : ["Yes","GENPROF"],
    "A derivative of Ubuntu made to be more user-friendly is called..." : ["Linux Mint","GENPROF"]
}

// Stores all the questions from the dictionary into a list
var Q_bank = Object.keys(questions)

// test Q_bank
console.log(Q_bank)

//defines current Question bank + number of questions for quiz
cur_Qbank =[]
window.a = 4

while (a > 0) {
    // randomly assigns questions to the bank that will be used for this iteration of the quiz
    cur_Qbank.push(Pick_Random_Value(Q_bank));
    a -= 1;
}

console.log(cur_Qbank)



// sets user score and mod scores to 0
var user_score = 0
var code_score = 0
var genProf_score = 0
var genProf_total = 0
var code_total = 0

// globally defines the right_ans variable as a list and a
window.right_ans = []
var i = 0

// Loops for each question in the current bank for this quiz
for (const item of cur_Qbank) {
    // test for ensuring variables store correctly
    console.log(item)
    console.log("Question"+i)
    console.log(i)

    // Setting each fo the question in the front end to the respective question
    document.getElementById("Q"+i).innerHTML = item

    //test to ensure questions store appropriately
    console.log(document.getElementById("Q"+i).innerHTML)

    // add each correct answer to the right_ans list
    right_ans.push(questions[item])

    // iterates loop
    i++
}

// test for final result with correct answers
console.log(right_ans)
```

### Javascript for Checking Answer
```

//function to check the answers the user puts in
function CheckAns(review_type) {
    b = 0

    console.log(b)

    console.log("rights answer test: " + right_ans)
    console.log(right_ans[0])


    for ( const item of right_ans) {
        console.log("A"+String(b))
        // Sets the user's answer to lowercase to prevent mismatch due to improper capitalization
        var user_ans = (document.getElementById("A"+String(b)).value).toLowerCase()
        console.log(user_ans)

        // sets right answer to the current correct answer for this particualr question
        var cur_right_ans = right_ans[b]
        console.log(String(cur_right_ans[0]).toLowerCase())

        // Sets to simple grading mode
        if (review_type === "simple") {
            // checks if answer is correct
            if (user_ans === String(cur_right_ans[0]).toLowerCase()) {
                document.getElementById("I" + String(b)).innerHTML = "That's Correct"

                user_score += 1
            } else {
                // Marks question as incorrect
                document.getElementById("I" + String(b)).innerHTML = "That's Incorrect.The right answer is: " + String(cur_right_ans[0])
            }
        // Sets to complex Grading mode
        } else if (review_type === "complex"){
            // checks if answer is correct
            if (user_ans === String(cur_right_ans[0]).toLowerCase()) {
                document.getElementById("I"+String(b)).innerHTML = "That's Correct"

                user_score += 1
                // checks additional modifiers and adds score+total accordingly
                if (cur_right_ans[1] === "GENPROF") {
                    genProf_total++
                    genProf_score++
                } else if (cur_right_ans[1] === "CODE") {
                    code_total++
                    code_score++
                } else {

                }

            } else {
                // Marks question as incorrect
                document.getElementById("I"+String(b)).innerHTML = "That's Incorrect.The right answer is: "+String(cur_right_ans[0])

                // Adds to total number of certain question asked
                if (cur_right_ans[1] === "GENPROF") {
                    genProf_total++
                } else if (cur_right_ans[1] === "CODE") {
                    code_total++
                } else {

                }
            }
        } else {
            alert("This isnt supposed to happen. Error in webpage")
        }

        b++
    }
    //test total scores
    console.log(user_score)
    console.log(code_score)
    console.log(genProf_score)

    // Displays scores to over total
    if (review_type === "simple") {
        document.getElementById("total_scr").innerHTML = String(user_score)+"/"+String(b)
        document.getElementById("code_scr").innerHTML = "Not evaluated"
        document.getElementById("genProf_scr").innerHTML = "Not evaluated"
    } else if (review_type === "complex") {
        document.getElementById("total_scr").innerHTML = String(user_score)+"/"+String(b)
        document.getElementById("code_scr").innerHTML = String(code_score)+"/"+String(code_total)
        document.getElementById("genProf_scr").innerHTML = String(genProf_score)+"/"+String(genProf_total)
    } else {
        alert("You found the secret error that isn't supposed to happen")
    }


}
```

## 2.Video 
### **Video** : https://www.youtube.com/embed/dGm9PNfEykg


## 3.Written Response 

### 3A

**i** - This program is a series of questions that will attempt to discern how well a user is versed in Linux. The user will be able to understand how well they understand linux both in terms of understanding the linux terminal and their general understanding of Linux.

**i** - In the video, the page refreshed and switched the questions shown indicating the randomization aspect of the program. In addition, there were text areas for a user to enter their answers, and the answers were also evaluated as shown by the various scores that a user could receive. In addition, the program could also conduct two forms of review, one of which just gave the users total score, while the other “complex” review was able to give a breakdown on what type of question the user missed, whether that be general knowledge or linux terminal specific. The users were also told what questions they got wrong and right, and the ones they got wrong, they were shown the right answer. 

**iii** - The input is taken from the user entering into the textboxes and pressing either submit button. This then returns the user's score, what they got wrong and what they got right, and their subscores(should they have chosen the complex review option) 

### 3B
 
**i** - 

```
var questions = {
    "What is the most universal command to access root privilages?": ["sudo","CODE"],
    "What does FOSS stand for?" : ["Free and Open Source Software","GENPROF"],
    "Linux is a(n)..." : ["kernel","GENPROF"],
    "What is the name of the place that RMS belongs?" : ["GNU","CODE"],
    "Which of the following characters can combine several commands?" : ["pipe - |","CODE"],
    "Can Linux can run on every computer?" : ["Yes","GENPROF"],
    "A derivative of Ubuntu made to be more user-friendly is called..." : ["Linux Mint","GENPROF"]
}

// Stores all the questions from the dictionary into a list
var Q_bank = Object.keys(questions)

// test Q_bank
console.log(Q_bank)

//defines current Question bank + number of questions for quiz
cur_Qbank =[]
window.a = 4

while (a > 0) {
    // randomly assigns questions to the bank that will be used for this iteration of the quiz
    cur_Qbank.push(Pick_Random_Value(Q_bank));
    a -= 1;
}


```

**ii** - 
```
for (const item of cur_Qbank) {
    // test for ensuring variables store correctly
    console.log(item)
    console.log("Question"+i)
    console.log(i)

    // Setting each fo the question in the front end to the respective question
    document.getElementById("Q"+i).innerHTML = item

    //test to ensure questions store appropriately
    console.log(document.getElementById("Q"+i).innerHTML)

    // add each correct answer to the right_ans list
    right_ans.push(questions[item])

    // iterates loop
    i++
}

```

**iii** - The name of the list in this program is cur_Qbank. 

**iv** - The data contained in cur_Qbank represents the questions that will be displayed on the users frontend from the dictionary used in the first segment of code, which acts as a sort of mass question bank. The question is cur_Qbank is then assigned to the html frontend to be displayed to the user. The data in this list is a set of strings which contain the questions. In addition, the loop in code segment two displays how the questions bank is being used with the original dictionary to locate the values for the keys, in this instance the answers for the questions. These are then stored into a separate list to be used for another function. 

**v** - A list was used here instead of directly pulling from the dictionary as any randomizers using javascript are easier to execute,  both in terms of ease of coding and strain on the computer when using lists vs dictionaries as there is less to sort though in both instances. Trying to randomize using a dictionary in Javascript is extremely difficult and would make the code less efficient. But it is possible to use the dictionary instead by randomly selecting keys from the dictionary. 


### 3C 

**i** - 
```
function CheckAns(review_type) {
    b = 0

    console.log(b)

    console.log("rights answer test: " + right_ans)
    console.log(right_ans[0])


    for ( const item of right_ans) {
        console.log("A"+String(b))
        // Sets the user's answer to lowercase to prevent mismatch due to improper capitalization
        var user_ans = (document.getElementById("A"+String(b)).value).toLowerCase()
        console.log(user_ans)

        // sets right answer to the current correct answer for this particualr question
        var cur_right_ans = right_ans[b]
        console.log(String(cur_right_ans[0]).toLowerCase())

        // Sets to simple grading mode
        if (review_type === "simple") {
            // checks if answer is correct
            if (user_ans === String(cur_right_ans[0]).toLowerCase()) {
                document.getElementById("I" + String(b)).innerHTML = "That's Correct"

                user_score += 1
            } else {
                // Marks question as incorrect
                document.getElementById("I" + String(b)).innerHTML = "That's Incorrect.The right answer is: " + String(cur_right_ans[0])
            }
        // Sets to complex Grading mode
        } else if (review_type === "complex"){
            // checks if answer is correct
            if (user_ans === String(cur_right_ans[0]).toLowerCase()) {
                document.getElementById("I"+String(b)).innerHTML = "That's Correct"

                user_score += 1
                // checks additional modifiers and adds score+total accordingly
                if (cur_right_ans[1] === "GENPROF") {
                    genProf_total++
                    genProf_score++
                } else if (cur_right_ans[1] === "CODE") {
                    code_total++
                    code_score++
                } else {

                }

            } else {
                // Marks question as incorrect
                document.getElementById("I"+String(b)).innerHTML = "That's Incorrect.The right answer is: "+String(cur_right_ans[0])

                // Adds to total number of certain question asked
                if (cur_right_ans[1] === "GENPROF") {
                    genProf_total++
                } else if (cur_right_ans[1] === "CODE") {
                    code_total++
                } else {

                }
            }
        } else {
            alert("This isnt supposed to happen. Error in webpage")
        }

        b++
    }
    //test total scores
    console.log(user_score)
    console.log(code_score)
    console.log(genProf_score)

    // Displays scores to over total
    if (review_type === "simple") {
        document.getElementById("total_scr").innerHTML = String(user_score)+"/"+String(b)
        document.getElementById("code_scr").innerHTML = "Not evaluated"
        document.getElementById("genProf_scr").innerHTML = "Not evaluated"
    } else if (review_type === "complex") {
        document.getElementById("total_scr").innerHTML = String(user_score)+"/"+String(b)
        document.getElementById("code_scr").innerHTML = String(code_score)+"/"+String(code_total)
        document.getElementById("genProf_scr").innerHTML = String(genProf_score)+"/"+String(genProf_total)
    } else {
        alert("You found the secret error that isn't supposed to happen")
    }


}
```

**ii** -
```
        <h3 id="Q3"></h3>
        <input type = "text" id="A3">
        <h5 id="I3"></h5>

        <br>


        <input type = "button" onclick="CheckAns('simple')" value="Simple Review!">
```

**iii** - The function listed here is used to check the user’s answer against the correct answer for each question and then add a point to their overall score if they get it right. If the complex review was selected, the program will also additionally tally up the total number of questions which are terminal related and how many the user got right out of those as well as the number of questions which are generally about linux and how many the user got right out of those. It then displays the scores over their totals. 

**iv** - First create a variable to keep count of the loop. Then set a variable to the user’s entry from the html code. Then proceed to set another variable as the right answer from the list of right answers with an index matching the number of the variable keeping count of the loop number. Then determine if the parameter passed for the function is “simple” or “complex”. If it’s check if the variable storing the user answer matches the correct answer, if it does change the html element to the right of the textbox to say that the answer is correct. Otherwise set it to not correct and display the right answer as well. If the answer is complex, repeat the above steps but if the user gets it right, determine if the question is regarding linux terminal or general information about linux. Then increase the score variable for the corresponding sub-term, and the total for that. Increase the total even if the answer is incorrect. Then set the scores in the html frontend equal to the score over the score total per subcategory and the overall score. 


### 3D

**i**  -
The first call represents when the scoring is conducted just with the total overall score when the parameter, review_type, is set to “simple” This is set by the button labeled “simple review” and it runs the function with the respective review_type parameter being set to “simple” 

The second call represents when the scoring is conducted with the total score and the sub-scores also being calculated when the parameter, review_type, is set to “complex” This is set by the button labeled “complex review” and it runs the function with the respective review_type parameter being set to “complex” 

**ii** -
The first call checks if the parameter is passed as “simple” in which case it will execute the scoring part of the algorithm that is covered in the “simple” if statement tree

The second call checks if the parameter passed is “complex” in which case it will execute the scoring part of the algorithm that is covered in the “complex” if statement tree.

**iii** - 
The first call will return only the total score over the total number of questions(which is always five) and will return “not evaluated” for all other sub scores. 

The second call will return the total score over the total number of questions and the individual subscores for Linux terminal proficiency and general linux info proficiency over their respective calculated totals. 





