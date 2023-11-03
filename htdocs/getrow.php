<?php

$data = file_get_contents("php://input");
$row = json_decode($data, TRUE);

$name = $row['NAME'];
$age = $row['AGE'];
$gender = $row['GENDER'];
$country = $row['COUNTRY'];
$job = $row['JOB'];
$email = $row['EMAIL'];
$phone = $row['PHONE'];


if(!empty($name)){
$dbFile = "register.db";
$db = new PDO("sqlite:$dbFile");

$db->exec("INSERT INTO Contact (EMAIL, PHONE) VALUES ('$email', '$phone');") or die(print_r($db->errorInfo(), true));
$coid = $db->lastInsertId();

$db->exec("INSERT INTO Info (COUNTRY, JOB, CO_ID) VALUES ('$country', '$job', '$coid');") or die(print_r($db->errorInfo(), true));
$infoid = $db->lastInsertId();

$db->exec("INSERT INTO Customer (NAME, AGE, GENDER, INFO_ID) VALUES ('$name', '$age', '$gender', '$infoid');") or die(print_r($db->errorInfo(), true));
$cuid = $db->lastInsertId();

}

?>
