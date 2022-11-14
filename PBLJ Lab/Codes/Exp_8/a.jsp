<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<%
		String str = request.getParameter("t1");
		
		String s = "";
		int n = str.length();
		boolean table[][] = new boolean[n][n];
		int maxLength = 1;
		for (int i = 0; i < n; i++) table[i][i] = true;
	
		int start = 0;
		for (int i = 0; i < n - 1; i++) {
			if (str.charAt(i) == str.charAt(i + 1)) {
				table[i][i + 1] = true;
				start = i;
				maxLength = 2;
			}
		}
		
		for (int k = 3; k <= n; k++) {
			for (int i = 0; i < n - k + 1; i++) {
				int j = i + k - 1;
				if (table[i + 1][j - 1] && str.charAt(i) == str.charAt(j)) {
					table[i][j] = true;
					s = str.charAt(i) + s;
					if (k > maxLength) {
						start = i;
						maxLength = k;
					}
				}
			}
		}
		
		%>
		
		<h3>Length of palindrome subseqnce: <%=s.length()%></h3>
</body>
</html>