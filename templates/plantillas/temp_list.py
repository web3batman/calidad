<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>MATRIZ</title> 
<script type="text/javascript" src="http://code.jquery.com/jquery-1.5.min.js"></script>  
<script type="text/javascript" src="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.js"></script>
<link rel="stylesheet"  href="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.css" /> 
</head>
<style type='text/css'>
.split-button-custom {
    float: right;
    margin-right: 10px;
    margin-top: -32px;
    border-bottom-left-radius: 1em 1em;
    border-bottom-right-radius: 1em 1em;
    border-top-left-radius: 1em 1em;
    border-top-right-radius: 1em 1em;   
}

.split-button-custom span.ui-btn-inner {
    border-bottom-left-radius: 1em 1em;
    border-bottom-right-radius: 1em 1em;
    border-top-left-radius: 1em 1em;
    border-top-right-radius: 1em 1em;
    padding-right: 0px;
}

.split-button-custom span.ui-icon {
    margin-top: 0px;
    right: 0px;
    top: 0px;
    position: relative;
}
</style>
<body>

<section id="page1" data-role="page">  
    <header data-role="header">  
        <h1>Página 2</h1>  
    </header>  
    <div position=relative align=right data-role="controlgroup" data-type="horizontal">
        <a href="{{path}}/{{name}}_new" data-role="button">Add</a>
    </div>
    <ul data-role="listview" data-filter="true" data-theme="b" style="margin-bottom: 50px;">
    {{'{%if table %}'}}
        {{'{%for a in table %}'}}
          <li>
            <a href="/{{name_anterior}}_list?{{name}}_id={{'{{'}} a.id {{'}}'}}">
              <h3>{{'{{'}}a.{{name}}{{'}}'}}</h3>
            </a>
            <a href="/{{name}}_edit?id={{'{{'}} a.id {{'}}'}}" class="split-button-custom" data-role="button" data-icon="arrow-r" data-iconpos="notext">Editar</a>
            <a href="/{{name}}_delete?id={{'{{'}} a.id {{'}}'}}" class="split-button-custom" data-role="button" data-icon="gear" data-iconpos="notext">Borrar</a>
            <a href="#" style="display: none;">Dummy</a>
          </li>
        {{'{%endfor%}'}}
    {{'{%endif%}'}}
    </ul>
    <footer data-role="footer">  
        Pie de la página 2  
    </footer>  
</section> 

</body>
</html>