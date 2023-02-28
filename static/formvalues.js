function testResults()
    {    
        //gettting the values
        var name = document.getElementById("name").value;
        var diet= document.getElementById("diet").value; 
        var alcohol= document.getElementById("alcohol").value; 
        var pollution= document.getElementById("pollution").value; 
        //saving the values in local storage
        localStorage.setItem("name", name);
        localStorage.setItem("diet", diet);
        localStorage.setItem("alcohol", alcohol);
        localStorage.setItem("pollution", pollution);   
    }