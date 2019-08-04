<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>MATRIZ</title> 
<script type="text/javascript" src="http://code.jquery.com/jquery-1.5.min.js"></script>  
<script type="text/javascript" src="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.js"></script>
<link rel="stylesheet"  href="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.css" /> 
</head>
<body>

<section id="page1" data-role="page">  
    <header data-role="header">  
        <h1>Página 2</h1>  
    </header>  
    <div id="container">
    <form action="/{{name}}_new" method="post">
     <div id="inputs">
         <div><input name="id" type="text" value=""/></div>
{%-for form in dbform%}         
         <div><label for="{{form}}">{{form}}:</label><input name="{{form}}" type="text" value=""/></div>
{%-endfor%}
         <input type="submit" value="Guardar" />
      </div>
    </form>
    </div>
    <footer data-role="footer">  
        Pie de la página 2  
    </footer>  
</section> 

</body>
</html>