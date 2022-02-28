// Randomizer
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


