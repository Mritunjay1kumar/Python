//etner employee details and  store them and display them

import java.sql.*;
import java.util.*;

class Employee
{
	public static void main(String ar[])
	{
		Scanner sc = new Scanner(System.in);
		int eid;
		String ename,desg;
		float salary;

		Connection con;
		Statement st;
		ResultSet rs;
		String s;

		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String uname = "SYSTEM";
		String upass = "SYSTEM";

		System.out.println("enter Employee Details");
		eid = sc.nextInt();
		ename = sc.next();
		desg = sc.next();
		salary = sc.nextFloat();
	
		
		try
		{
			Class.forName(driver);
		}
		catch(ClassNotFoundException e)
		{
			System.out.println(e);
		}
		try
		{
			con = DriverManager.getConnection(url,uname,upass);
			st  = con.createStatement();
			s = "insert into emp values(" + eid + ",'" + ename+ "','" + desg + "'," + salary + ")";
			st.executeUpdate(s);
			s =  "select * from emp";
			rs  = st.executeQuery(s);
			while(rs.next())
			{
				System.out.println(rs.getInt(1)+ "  " + rs.getString(2)+"  " + rs.getString(3)+"  " + rs.getFloat(4)); 
			}
			con.close();
			st.close();
		}
		catch(SQLException e)
		{
			System.out.println(e);
		}
	}
		
}