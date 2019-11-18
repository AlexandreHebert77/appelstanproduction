# AppelStan
# Python générateur de fiches d'identité
#
# Alexandre Hébert & Joseph de Gaullier
# appelstan1920@gmail.com
# ©AppelStan

for n in range(1,225):

	#CREATION DOC
	nomfichier = 'place' + str(n) + '.html'
	monfichier = open(nomfichier,'x')
	monfichier.close
	#REMPLISSAGE
	monfichier = open(nomfichier, 'a')
	monfichier.write("<!doctype html>")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n <html lang="en">')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n   <head>")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n     <meta charset="utf-8">')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n     <link rel="stylesheet" href="style.css">')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n     <title>')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n       Interne')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n     </title>')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n   </head>')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n   <body id="body">')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n <?php")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n include("fonctions.php");')
	monfichier.close
	
	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ?>")
	monfichier.close
	
	monfichier = open(nomfichier, 'a')
	monfichier.write('\n <?php')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	txt = '	$Place=' + str(n) + ';'
	monfichier.write("\n " + txt)
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n     connectMaBase();")
	monfichier.close
	
	monfichier = open(nomfichier, 'a')
	monfichier.write("\n     $sql = 'SELECT Nom, Prenon, Classe WHERE Place = $Place';")
	monfichier.close


	monfichier = open(nomfichier, 'a')
	monfichier.write('\n 	mysql_close();')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n 	mysql_query ($sql) or die ('Erreur SQL !');")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ?>")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n     <!-- Ici tu ajoutes le nom de l'interne -->")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n     <h1><?php echo $sql[Nom] $sql[Prenom] ?></h1>")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n     <!-- Ici la classe de l'interne -->")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n     <p><?php echo $Classe[Classe] ?> </p>")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n <!-- Ici la photo type identité (a voir  selon la taille de celle fournie)-->")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n <img src="images.png" alt="">')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n <a class="btn btn-success btn-lg btn-block" href="#" role="button"  style="margin-top:40px; margin-bottom:20px">Présent</a>')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n <a class="btn btn-danger btn-lg btn-block" href="#" role="button"  style="margin-top:20px">Retardataire</a>')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n ')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n <footer class="sticky-top" style="margin-top:70px">')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n <p style="color:#FFF; font-size:10px">Tous droits réservés</p>')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n </footer>')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n     <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n     <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-O2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>')
	monfichier.close


	monfichier = open(nomfichier, 'a')
	monfichier.write('\n     <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-jSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write('\n   </body>')
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n ")
	monfichier.close

	monfichier = open(nomfichier, 'a')
	monfichier.write("\n </html>")
	monfichier.close
