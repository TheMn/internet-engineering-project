function copy_to_clipboard() {
    /* Get the text field */
    var copyText = document.getElementById("url_to_copy");

    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/

    /* Copy the text inside the text field */
    document.execCommand("copy");

    /* Alert the copied text */
    alert("از طریق آدرس کپی شده می توانید اطلاعات خود را ویرایش کنید");
}

$(document).ready(function () {
    console.log('salam');
    $('#div-1-next').click(function () {
        $("#form-part-1").css("display", "none");
        $("#form-part-2").css("display", "flex");
        scroll("#form-part-2");
    });
    $('#div-2-next').click(function () {
        $("#form-part-2").css("display", "none");
        $("#form-part-3").css("display", "flex");
        scroll("#form-part-3");
    });
    $('#div-2-prev').click(function () {
        $("#form-part-2").css("display", "none");
        $("#form-part-1").css("display", "flex");
        scroll("#form-part-1");
    });
    $('#div-3-next').click(function () {
        $("#form-part-3").css("display", "none");
        $("#form-part-4").css("display", "flex");
        scroll("#form-part-4");
    });
    $('#div-3-prev').click(function () {
        $("#form-part-3").css("display", "none");
        $("#form-part-2").css("display", "flex");
        scroll("#form-part-2");
    });
    $('#div-4-next').click(function () {
        $("#form-part-4").css("display", "none");
        $("#form-part-5").css("display", "flex");
        scroll("#form-part-5");
    });
    $('#div-4-prev').click(function () {
        $("#form-part-4").css("display", "none");
        $("#form-part-3").css("display", "flex");
        scroll("#form-part-3");
    });
    $('#div-5-prev').click(function () {
        $("#form-part-5").css("display", "none");
        $("#form-part-4").css("display", "flex");
        scroll("#form-part-4");
        $("#error-container").empty();
    });
    $("#save").click(function () {
        $("#error-container").empty();
        let student_picture = $("#id_student_picture");
        let melli_code = $("#id_melli_code").val();
        if (!validateMelliCode(melli_code)) {
            alert('کد ملی نامعتبر است.');
            event.preventDefault()
        } else if (student_picture.files !== undefined && student_picture.files[0].size > 500000) {
            alert("حجم عکس بیش از حد مجاز است.");
            event.preventDefault()
        } else {
            $("#my_form").submit();
        }
    });

    function validateMelliCode(melliCode) {

        if (melliCode.length !== 10) {
            return false; // Melli Code is less or more than 10 digits
        } else {
            let sum = 0;

            for (let i = 0; i < 9; i++) {
                sum += parseInt(melliCode.charAt(i)) * (10 - i);
            }

            let lastDigit;
            let divideRemaining = sum % 11;

            if (divideRemaining < 2) {
                lastDigit = divideRemaining;
            } else {
                lastDigit = 11 - (divideRemaining);
            }

            if (parseInt(melliCode.charAt(9)) === lastDigit) {
                return true;
            } else {
                return false; // Invalid MelliCode
            }
        }
    }

    $('#id_student_picture').bind('change', function () {
        if (this.files[0].size > 500000) {
            alert('حجم فایل بیش از حد مجاز است');
        }

    });
    $("#id_ss, #id_ss_id, #id_ss_numerical , #id_father_job_phone, #id_mother_job_phone, #id_home_phone, #id_father_phone, #id_mother_phone ,#id_this_child_counter, #id-family_members_counter").on("keypress keyup blur", function (event) {
        $(this).val($(this).val().replace(/[^\d].+/, ""));
        if ((event.which < 48 || event.which > 57)) {
            event.preventDefault();
        }
    });
    $("id_grade_at_9th").on("keypress keyup blur", function (event) {
        //this.value = this.value.replace(/[^0-9\.]/g,'');
        $(this).val($(this).val().replace(/[^0-9\.]/g, ''));
        if ((event.which != 46 || $(this).val().indexOf('.') != -1) && (event.which < 48 || event.which > 57)) {
            event.preventDefault();
        }
    });

    let error_list = [];

    $("#main-save").click(function () {
        let student_name = $("#id_student_first_name");
        let student_last_name = $("#id_student_last_name");
        let student_picture = $("#id_student_picture");
        let student_shomare_shenasname = $("#id_ss");
        let student_shenasname_seri = $("#id_ss_id");
        let student_shenasname_adad = $("#id_ss_numerical");
        let student_shenasname_horof = $("#id_ss_alphabetical");
        let melli_code = $("#id_melli_code");
        // let birth_day = $("#id_birth_day");
        // let birth_month = $("#id_birth_month");
        // let birth_year = $("#id_birth_year");
        let birth_place_state = $("#id_birth_place_state");
        let birth_place_town = $("#id_birth_place_town");
        let birth_place_city = $("#id_birth_place_city");
        let religion = $("#id_religion");
        let nationality = $("#id_nationality");
        // let physical_situation = $("#id_physical_situation");
        // let left_handed = $("#id_left_handed");
        let father_first_name = $("#id_father_first_name");
        let father_edu = $("#id_father_edu");
        let father_job = $("#id_father_job");
        let father_job_place = $("#id_father_job_place");
        // let father_job_phone = $("#id_father_job_phone");
        let mother_edu = $("#id_mother_edu");
        let mother_job = $("#id_mother_job");
        // let mother_job_phone = $("#id_mother_job_phone");
        let home_location = $("#id_home_location");
        let home_phone = $("#id_home_phone");
        // let home_situation = $("#id_home_situation");
        let father_mail = $("#id_father_mail");
        let father_phone = $("#id_father_phone");
        let mother_mail = $("#id_mother_mail");
        let mother_phone = $("#id_mother_phone");
        // let homemate = $("#id_homemate");
        // let student_own_place = $("#id_student_own_place");
        let this_child_counter = $("#id_this_child_counter");
        let family_members_counter = $("#id_family_members_counter");
        // let student_have_reading_room = $("#id_student_have_reading_room");
        let student_mail = $("#id_student_mail");
        let student_phone = $("#id_student_phone");
        // let last_year_edu = $("#id_last_year_edu");
        let field_of_study = $("#id_field_of_study");
        // let field_of_olympiad = $("#id_field_of_olympiad");
        // let field_of_pajohesh = $("#id_field_of_olympiad");
        // let field_of_weakness = $("#id_field_of_weakness");
        let grade_at_9th = $("#id_grade_at_9th");
        let last_year_school_name = $("#id_last_year_school_name");
        // let last_year_school_code = $("#id_last_year_school_code");
        // let last_shahed_in_all_schools = $("#id_last_year_school_code");
        // let exceptional_student = $("#id_exceptional_student");
        // let extra_note = $("#id_extra_note");
        // let valid = true;

        if (student_name.val() === undefined || student_name.val().length === 0) {
            error("نام معتبر نیست.");
        }
        if (student_last_name.val() === undefined || student_last_name.val().length === 0) {
            error("نام خانوادگی معتبر نیست.");
        }
        if (student_picture.files !== undefined && student_picture.files[0].size > 500000) {
            error("حجم عکس بیش از حد مجاز است.");
        }
        if (student_shomare_shenasname.val() === undefined || !validateMelliCode(student_shomare_shenasname.val())) {
            error("شماره شناسنامه نا معتبر است.");
        }
        if (student_shenasname_seri.val() === undefined || student_shenasname_seri.val().length !== 6) {
            error("سریال ۶ رقمی شناسنامه نا معتبر است.");
        }
        if (student_shenasname_adad.val() === undefined || student_shenasname_adad.val().length !== 2) {
            error("سری ۲ رقمی شناسنامه نا معتبر است.");
        }
        if (student_shenasname_horof.val() === undefined || student_shenasname_horof.val().length === 0) {
            error("سری حروفی شناسنامه نا معتبر است.");
        }
        if (melli_code.val() === undefined || !validateMelliCode(melli_code.val())) {
            error("کد ملی نا معتبر است.");
        }
        if (birth_place_city.val() === undefined || birth_place_city.val().length === 0) {
            error("شهر محل تولد نا معتبر است.");
        }
        if (birth_place_town.val() === undefined || birth_place_town.val().length === 0) {
            error("استان محل تولد نا معتبر است.");
        }
        if (birth_place_state.val() === undefined || birth_place_state.val().length === 0) {
            error("شهرسنان محل تولد نا معتبر است.");
        }
        if (student_shenasname_adad.val() === undefined || student_shenasname_adad.val().length !== 2) {
            error("سری ۲ رقمی شناسنامه نا معتبر است.");
        }
        if (nationality.val() === undefined || nationality.val().length === 0) {
            error("ملیت نا معتبر است.");
        }
        if (religion.val() === undefined || religion.val().length === 0) {
            error("دین نا معتبر است.");
        }
        if (father_first_name.val() === undefined || father_first_name.val().length === 0) {
            error("نام پدر نا معتبر است.");
        }
        if (father_edu.val() === undefined || father_edu.val().length === 0) {
            error("تحصیلات پدر نا معتبر است.");
        }
        if (father_job.val() === undefined || father_job.val().length === 0) {
            error("شغل پدر نا معتبر است.");
        }
        if (father_job_place.val() === undefined || father_job_place.val().length === 0) {
            error("محل کار  پدر نا معتبر است.");
        }
        if (mother_edu.val() === undefined || mother_edu.val().length === 0) {
            error("تحصیلات مادر نا معتبر است.");
        }
        if (mother_job.val() === undefined || mother_job.val().length === 0) {
            error("شغل مادر نا معتبر است.");
        }
        if (home_location.val() === undefined || home_location.val().length === 0) {
            error("آدرس منزل نا معتبر است.");
        }
        if (home_phone.val() === undefined || home_phone.val().length === 0) {
            error("شماره منزل نا معتبر است.");
        }
        if (father_mail.val().length !== 0 && !isEmail(father_mail.val())) {
            error("ایمیل پدر نا معتبر است.");
        }
        if (mother_mail.val().length !== 0 && !isEmail(mother_mail.val())) {
            error("ایمیل مادر نا معتبر است.");
        }
        if (father_phone.val() === undefined || father_phone.val().length !== 11) {
            error("شماره موبایل پدر نا معتبر است.");
        }
        if (mother_phone.val() === undefined || mother_phone.val().length !== 11) {
            error("شماره موبایل مادر نا معتبر است.");
        }
        if (this_child_counter.val() === undefined || this_child_counter.val().length === 0) {
            error("چندمین فرزند است  نا معتبر است.");
        }
        if (family_members_counter.val() === undefined || family_members_counter.val().length === 0) {
            error("تعداد اعضای خانواده نا معتبر است.");
        }
        if (student_mail.val() === undefined || !isEmail(student_mail.val())) {
            error("ایمیل دانش آموز  نا معتبر است.");
        }
        if (student_phone.val() === undefined || student_phone.val().length !== 11) {
            error("شماره موبایل دانش آموز نا معتبر است.");
        }
        if (field_of_study.val() === undefined || field_of_study.val().length === 0) {
            error("رشته مورد علاقه نا معتبر است.");
        }
        if (grade_at_9th.val() === undefined || grade_at_9th.val().length === 0) {
            error("معدل کل  نا معتبر است.");
        }
        if (last_year_school_name.val() === undefined || last_year_school_name.val().length === 0) {
            error("نام مدرسه قبلی  نا معتبر است.");
        }
        if (error_list.length === 0)
            $("#my_form").submit();
        else {
            event.preventDefault();
            show_error_list();
        }

    });

    function isEmail(email) {
        let regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if (!regex.test(email)) {
            return false;
        } else {
            return true;
        }
    }

    function error(message) {
        error_list[error_list.length] = message;
    }

    $(window).keydown(function (event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            return false;
        }
    });

    function show_error_list() {
        let error_element = "";
        error_list.forEach(function (item) {
            error_element += "<div dir ='rtl' class='alert alert-danger text-right'><strong>" + item + "  </strong></div>\n";
        })
        $("#error-container").append(error_element)
        error_list = [];
    }

    function scroll(id) {
        $('html, body').animate({
            scrollTop: $(id).offset().top - 100
        });
    }

});