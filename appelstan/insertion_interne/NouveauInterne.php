<?php
function connectMaBase(){
    $base = mysql_connect ('localhost', 'Appel', 'Appel');  
    mysql_select_db ('ETUDE', $base) ;
}
?>