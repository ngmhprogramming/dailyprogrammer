<?php
function details(){
    $name = readline("What is your name? ");
    $age = readline("What is your age? ");
    $username = readline("What is your reddit username? ");
    echo("Your name is $name, you are $age years old, and your username is $username!");
    file_put_contents("php_easy_1_details.txt", "$name $age $username" | FILE_APPEND);
}

if(get_included_files()[0] == __FILE__){
    details();
}
?>