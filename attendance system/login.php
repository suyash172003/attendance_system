<?php
$aa=$_POST['a'];
$bb=$_POST['b'];
$cc=$_POST['c'];
$dd=$_POST['d'];
mysql_connect("localhost","root","");
mysql_select_db("data");
$query="INSERT INTO student VALUES('$aa','$bb','$cc','$dd')";
mysql_query($query);

echo "database update ho gaya";

?>