setInterval(myFun, 1000)

function myFun(){
    var hour = document.getElementById('hour')
    var minute = document.getElementById('minute')
    var second = document.getElementById('second')
    var d = new Date()
    var hr = d.getHours()
    var min = d.getMinutes()
    var sec = d.getSeconds()

    var sec_rotation = 6 * sec;
    var min_rotation = 6 * min
    var hr_rotation = 30 * hr + min / 2

    hour.style.transform = `rotate(${hr_rotation}deg)`
    minute.style.transform = `rotate(${min_rotation}deg)`
    second.style.transform = `rotate(${sec_rotation}deg)`

    
}