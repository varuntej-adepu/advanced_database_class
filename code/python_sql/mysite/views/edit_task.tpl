<p>Add a new task to the ToDo list:</p>
<form action="/edit" method="POST">
    <input type="hidden" name="id" value="{{id}}">
    <p>Edit task #{{id}}:</p>
    <br/>
	<input type="text" name="task" value="{{task}}">
    <br/>
    <p>Do you want to update this task?</p>
	<input type="submit" name="Yes" value="Yes">
	<input type="submit" name="No" value="No">
</form>
