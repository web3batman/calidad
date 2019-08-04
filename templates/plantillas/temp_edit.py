<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/fabric.js/3.0.0/fabric.min.js"></script>
<script type="text/javascript" src="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.js"></script>
<link rel="stylesheet"  href="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.css" /> 
<script type="text/javascript" src="http://code.jquery.com/jquery-1.5.min.js"></script>
</head>
<body>
<section id="page1" data-role="page">  
    <header data-role="header">  
        <h1>Pagina 2</h1>  
    </header> 
    <div id="container">
    <form action="/{{name}}_edit" method="post">
     <div id="inputs">
             <div><input name="id" type="hidden" value="{{ '{{' }}val.id{{ '}}' }}"/></div>
{%-for form in dbform%}               
             <div><label for="{{form}}">{{form}}:</label><input name="{{form}}" type="text" value="{{ '{{' }}val.{{form}}{{ '}}' }}"/></div>
{%-endfor%}
         <input type="submit" value="Guardar" />
      </div>
    </form>
    </div>
    <footer data-role="footer">  
        Pie de la pagina 2  
    </footer>  
</section>  
</body>
</html>
