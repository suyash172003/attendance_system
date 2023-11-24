<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table>
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