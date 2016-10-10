<p>Add a new task to the ToDo list:</p>
<form action="/delete" method="POST">
    <input type="hidden" name="id" value="{{id}}">
    <p>Do you want to delete this task?</p>
    <br/>
    <p><em>#{{id}}: {{task}}</em></p>
    <br/>
	<input type="submit" name="Yes" value="Yes">
	<input type="submit" name="No" value="No">
</form>