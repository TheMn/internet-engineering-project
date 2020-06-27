week = new Array("يكشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنج شنبه", "جمعه", "شنبه")
months = new Array("فروردين", "ارديبهشت", "خرداد", "تير", "مرداد", "شهريور", "مهر", "آبان", "آذر", "دي", "بهمن", "اسفند");
a = new Date();
d = a.getDay();
day = a.getDate();
month = a.getMonth() + 1;
year = a.getFullYear()
year = (year == 0) ? 2000 : year;
(year < 1000) ? (year += 1900) : true;
year -= ((month < 3) || ((month == 3) && (day < 21))) ? 622 : 621;
switch (month) {
    case 1:
        ((year-1) % 4) ? ((day < 20) ? (month = 10, day += 11) : (month = 11, day -= 19)) : ((day < 21) ? (month = 10, day += 10) : (month = 11, day -= 20));
        break;
    case 2:
        ((year-1) % 4) ? ((day < 19) ? (month = 11, day += 12) : (month = 12, day -= 18)) : ((day < 20) ? (month = 11, day += 11) : (month = 12, day -= 19));
        break;
    case 3:
        (year % 4) ? ((day < 20) ? (month = 12, day += 10) : (month = 1, day -= 19)) : ((year-1 % 4) ?((day < 21) ? (month = 12, day += 10) : (month = 1, day -= 20)):((day < 21) ? (month = 12, day += 9) : (month = 1, day -= 20)));
        break;
    case 4:
        (year % 4) ? ((day < 20) ? (month = 1, day += 12) : (month = 2, day -= 19)) : ((day < 21) ? (month = 1, day += 11) : (month = 2, day -= 20));
        break;
    case 5:
    case 6:
        (year % 4) ? ((day < 21) ? (month -= 3, day += 11) : (month -= 2, day -= 20)) : ((day < 22) ? (month -= 3, day += 10) : (month -= 2, day -= 21));
        break;
    case 7:
    case 8:
    case 9:
        (year % 4) ? ((day < 22) ? (month -= 3, day += 10) : (month -= 2, day -= 21)) : ((day < 23) ? (month -= 3, day += 9) : (month -= 2, day -= 22));
        break;
    case 10:
        (year % 4) ? ((day < 22) ? (month = 7, day += 9) : (month = 8, day -= 21)) : ((day < 23) ? (month = 7, day += 8) : (month = 8, day -= 22));
        break;
    case 11:
    case 12:
        (year % 4) ? ((day < 21) ? (month -= 3, day += 10) : (month -= 2, day -= 20)) : ((day < 22) ? (month -= 3, day += 9) : (month -= 2, day -= 21));
        break;
    default:
        break;
}
document.getElementById("date_place").innerHTML = " " + week[d] + " " + day + " " + months[month - 1] + " " + year;
