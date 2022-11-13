<%-- <%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%> --%>
<!DOCTYPE html>
<html>
<head>
<%-- <meta charset="ISO-8859-1"> --%>
<title>Calculator</title>
</head>
<body>
	<div style="background-color:yellow; padding-left: 30%;">
		<h1 style="padding-left: 10%">Calculator</h1>
		<form method="post" action="a.jsp">
			<table>
				<tr>
					<td><input type="radio" name="a1" value="add" checked>Addition<br></td>
				</tr>
				<tr>
					<td><input type="radio" name="a1" value="sub" >Subtraction<br></td>
				</tr>
				<tr>
					<td><input type="radio" name="a1" value="mul" >Multiplication<br></td>
				</tr>
				<tr>
					<td><input type="radio" name="a1" value="div" >Division<br></td>
				</tr>
			</table>
						
			<br><br>
			
			<table>
				<tr>
					<th> Enter first Value: </th>
					<td> <input type="text" name="t1" value=""> <td>
				</tr>
				<tr>
					<th> Enter second Value: </th>
					<td> <input type="text" name="t2" value=""> <td>
				</tr>
				<tr>
					<th colspan="2" style="padding: 10px 0 0 40%;"> <input type="submit" name="result"> </th>
				</tr>
			</table>
		</form>
	</div>
</body>
</html>