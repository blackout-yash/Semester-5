<%@ page errorPage="error.jsp" %>
<%@ page language="java"%>
<%@ page import="java.lang.*"%>
<html>
<body>   
	<div style="background-color:yellow; text-align: center;">
	<h1>Result for <%=request.getParameter("a1")%></h1>
	<%
	int i = Integer.parseInt(request.getParameter("t1"));
	int j = Integer.parseInt(request.getParameter("t2"));
	int k = Integer.MAX_VALUE;
    
	String str = request.getParameter("a1");
    if(str.equals("add")) k = i + j;
    if(str.equals("sub")) k = i - j;
	if(str.equals("mul")) k = i * j;
	if(str.equals("div")) k = i / j;
	%>
   	<h3> Result: <%=k%></h3>
    </div>
</body>
</html>