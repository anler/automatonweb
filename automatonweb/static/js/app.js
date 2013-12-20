(function ($) {
    $(document).ready(function () {
        var submit = $("#submit");

        $("#regex").on("keyup", function () {
            submit.click();
        });

        $("#automaton").ajaxForm(function (response) {
            var img = $("#automaton-image");
            img.attr("src", img.data("url") + "?t=" + new Date().getTime());
        });
    });
})(jQuery);
