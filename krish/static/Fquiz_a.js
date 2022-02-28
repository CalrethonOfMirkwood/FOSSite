
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