<div class="ui-grid-b">
{%for form in dbform%}
    <div class="ui-block-c">
    <div class="ui-bar ui-bar-c" style="height:60px;padding:0px">
       <fieldset data-role="controlgroup" data-type="horizontal" >
          <input type="checkbox" name="{{form[1]}}" id="{{form[1]}}" >
          <label for="{{form[1]}}" style="width: 90px"><font size="1" >{{form[0]}}</font></label>
      </fieldset>
    </div>
    </div>
{%endfor%}
</div>
