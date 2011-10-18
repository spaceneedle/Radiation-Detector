<?php

/* 

Radiation Detector 
Copyright 2011, Casey Halverson
MIT License (see README)

data collector for web server you want to publish data at.

This example script dumps data collected into a database.

*/

$api_key = "thisismyspecialkey";

import_request_variables("gP", "var_");

$cpm = $var_rad;
$epoc = $var_epoc;
$key = $var_key;

/* Sanity check */

if(strlen(cpm) > 50) { exit; }
if(strlen(epoc) >50) { exit; }
if($epoc == "") { exit; }
if($cpm == "") {exit; }

/* check our api key */

if($api_key != $key) { exit; }

/* escape stuff out to avoid basic injection techniques */

$cpm = pg_escape_string($cpm);
$epoc = pg_escape_string($epoc);

/* put it into a database, example is for postgres */

  $conn = pg_connect("dbname=mydatabase user=radiation password=radiationsucks2@$32432");
  $result = pg_query($conn, "INSERT into my_radiation_table VALUES(TIMESTAMPTZ 'epoch' + $epoc * '1 second'::interval,$cpm)");
  if (!$result) {
     echo "An error occured.\n";
     exit;
  }
  $trash = pg_fetch_all($result);

?>


