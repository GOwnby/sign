let form_count = Number($("[name=extra_field_count]").val());
// get extra form count so we know what index to use for the next item.
let limit = 12;
let count = 0;
$("#addOrg").click(function() {
    if (count > limit) {
        document.getElementById("MaxOrganizations").style.display = "block";
    } else {
        count ++;
        form_count ++;

        let element = $('<input type="text"/>');
        element.attr('name', 'extra_field_' + form_count);
        $("#form").append(element);
        // build element and append it to our forms container

        $("[name=extra_field_count]").val(form_count);
        // increment form count so our view knows to populate 
        // that many fields for validation
    }
})