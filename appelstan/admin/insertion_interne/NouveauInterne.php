<?php
function connectMaBase(){
    $base = mysql_connect ('localhost', 'mamp', '');  
    mysql_select_db ('ETUDE', $base) ;
}
?>
