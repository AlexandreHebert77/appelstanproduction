<!-- AppelStan
Mots de passe

Alexandre Hébert & Joseph de Gaullier
appelstan1920@gmail.com
©AppelStan -->

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>MDP pref ou pion et redirection</title>
    </head>
    <body>

        <?php
    if (isset($_POST['mot_de_passe']) AND $_POST['identifiant'] == "surveillant" AND $_POST['mot_de_passe'] ==  "surveillant") // Si le mot de passe est bon
    {
      header('Location:surveillant/new_2.html');
    exit();//redirection vers appel
    }
    if (isset($_POST['mot_de_passe']) AND $_POST['identifiant'] == "prefecture" AND $_POST['mot_de_passe'] ==  "prefecture")  // Si le mot de passe est bon
    {
      header('Location:admin/menu.html');
    exit();
    //redirection vers admin
    }
    else // Sinon, on affiche un message d'erreur
    {
        echo '<p>Mot de passe incorrect</p>';
    }
    ?>


    </body>
</html>
