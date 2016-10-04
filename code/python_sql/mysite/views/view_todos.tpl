%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p></p>
<table border="1">
%for row in rows:
	<tr>
	%id = int(row[0])
	%item = row[1]
	<td>{{item}}</td>
	<td><a href="/edit/{{id}}"><img src="/static/pencil.png" alt="edit" height="32" width="32"></a></td>
	<td><a href="/delete/{{id}}"><img src="/static/trashcan.png" alt="delete" height="32" width="32"></a></td>
	</tr>
%end
<tr>
    <td><i>Add another item...</i></td>
	<td><a href="/new"><img src="/static/pencil.png" alt="edit" height="32" width="32"></a></td>
</tr>
</table>