var jq = document.createElement('script');
jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(jq);

let applied = false;
attempts = 10
let count = 0
for(i=0; i<attempts; i++){
    setTimeout(function(){
        console.warn('Applying... |'+count)
        // Checks for element containing a form.
        if ($('body:contains("Continue")').length > 0) {
            NumericFieldInput()
            radioFieldInput()
            $('button:contains("Continue")').click();
        }

        // Supporting documents
        supportingDocuments()

        //Aplication
        SubmitTheApplication()

        // else if ($('html:contains("Your application has been submitted!")').length > 0) {
        //     $('title').text('Complete');
        // } 

        // after 10 failed entry attempts cancel it.
        if(count==attempts-1){
            $('title').text('Failed');
        }
        count += 1
        
    },5000*i+1);
}

function supportingDocuments(){
    if ($('body:contains("Consider adding supporting documents")').length > 0) {
        $('button:contains("Review your application")').click();
    } 
}

function SubmitTheApplication(){
    if ($('html:contains("Please review your application")').length > 0) {
        $('button:contains("Submit your application")').click();
    } 
}

function NumericFieldInput(){
    // checks for input
    $('input').each((index, element) => {
        question = $(element).closest('div.ia-Questions-item').text()
        if(question.includes('experience')){
            $(element).val(1)
        }
    });
}

function radioFieldInput(){
    // checks for label
    $('input').each((index, element) => {
        question = $(element).text()
        if(question.includes('commute or relocate')){
            $('label:contains("No")').click();
        }
    });
}