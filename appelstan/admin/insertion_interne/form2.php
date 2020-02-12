connexion.php

<?php
    $hote = 'localhost';
    $base = 'test';
    $user = 'root';
    $pass = '';
    $cnx = mysql_connect($hote, $user, $pass) or die(mysql_error());
    $ret = mysql_select_db($base) or die(mysql_error());
?>


transfert.php

<?php
    function transfert(){
        $ret        = false;
        $img_blob   = '';
        $img_taille = 0;
        $img_type   = '';
        $img_nom    = '';
        $taille_max = 250000;
        $ret        = is_uploaded_file($_FILES['fic']['tmp_name']);
        
        if (!$ret) {
            echo "Problème de transfert";
            return false;
        } else {
            // Le fichier a bien été reçu
            $img_taille = $_FILES['fic']['size'];
            
            if ($img_taille > $taille_max) {
                echo "Trop gros !";
                return false;
            }

            $img_type = $_FILES['fic']['type'];
            $img_nom  = $_FILES['fic']['name'];

            include ("connexion.php");
            $img_blob = file_get_contents ($_FILES['fic']['tmp_name']);

            $req = "INSERT INTO images (" .
            "img_nom, img_taille, img_type, img_blob " .
            ") VALUES (" .
            "'" . $img_nom . "', " .
            "'" . $img_taille . "', " .
            "'" . $img_type . "', " .
            "'" . addslashes ($img_blob) . "') ";

            $ret = mysql_query ($req) or die (mysql_error ());
return true;
    
        }
    }
?>

index.php 

<html>
   <head>
      <title>Stock d'images</title>
   </head>
   <body>
      <?php
         include ("transfert.php");
         if ( isset($_FILES['fic']) )
         {
             transfert();
         }
      ?>
      <h3>Envoi d'une image</h3>
      <form enctype="multipart/form-data" action="#" method="post">
         <input type="hidden" name="MAX_FILE_SIZE" value="250000" />
         <input type="file" name="fic" size=50 />
         <input type="submit" value="Envoyer" />
      </form>
      <p><a href="liste.php">Liste</a></p>
   </body>
</html>



list.php

<html>
   <head>
      <title>Stock d'images</title>
   </head>
   <body>
      <?php
         include ("connexion.php");
         $req = "SELECT img_nom, img_id " .
                "FROM images ORDER BY img_nom";
         $ret = mysql_query ($req) or die (mysql_error ());
         while ( $col = mysql_fetch_row ($ret) )
         {
             echo "<a href=\"apercu.php?id=" . $col[1] . "\">" . $col[0] . "</a><br />";
         }
      ?>
   </body>
</html>

apercu.php 


<?php
    
    if ( isset($_GET['id']) ){
        $id = intval ($_GET['id']);
        include ("connexion.php");
        $req = "SELECT img_id, img_type, img_blob " . 
               "FROM images WHERE img_id = " . $id;
        $ret = mysql_query ($req) or die (mysql_error ());
        $col = mysql_fetch_row ($ret);
        
        if ( !$col[0] ){
            echo "Id d'image inconnu";
        } else {
            header ("Content-type: " . $col[1]);
            echo $col[2];
        }

    } else {
        echo "Mauvais id d'image";
    }

?>


