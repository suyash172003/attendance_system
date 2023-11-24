<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="style.css">
    <title>Document</title>
	<style>
	.table1{
	width:60%;
	margin-left:auto;
	margin-right:auto;
	font-size:20px;
	border-collapse:collapse;
	box-shadow:0 20px 20px #ABB289;
	border-radius:8px 8px 6px 6px;
	overflow:hidden;
}
table1 thread tr{
	text-align:left;
	font-size:25px;
	font-weight:bolder;
	color:white;
	background-color:linear(#00A4EF,#000081);
}
.table1 th,.table1 td{
	padding:12px 15px;
}
.table1 tbody tr:nth-child(even){
	background-color:#eee;
}
.table1 tbody tr:nth-child(odd){
	background-color:#fff;
}
.table1 tbody tr:last-of-type{
	border-bottom:6px solid #00081;
}
.table1 tbody tr:hover{
	color:blue;
	font-weight:bold;
	border-top:2px solid blue;
	border-bottom:2px solid blue;
	cursor:progress;
	text-transform:uppercase;
}
</style>
	
</head>
<body>
    <table class ="table1">
        <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>ATTENDENCE</th>
        </tr>
        <?php
        $conn=mysqli_connect("localhost","root","","data2");
        if($conn->connect_error){
            die("Connection failed".$conn->connect_error);
        }
        $sql="SELECT id,name,attendence from student";
        $result=$conn->query($sql);
        if($result->num_rows>0)
        {
            while($row=$result->fetch_assoc())
			{
                echo "<tr><td>".$row["id"]."</td><td>".$row["name"]."</td><td>".$row["attendence"]."</td></tr>";
            }
            echo "</table>";
        }
        else{
            echo "0 result";
        }
        ?>
    </table>
</body>
</html>