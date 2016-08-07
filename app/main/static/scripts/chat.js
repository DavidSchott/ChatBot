var socket;
    $(document).ready(function() {
        hide_error();
        socket = io.connect('http://' + document.domain + ':' + location.port + '/chat');
        socket.on('connect', function() {
            socket.emit('joined', {});
        });
        socket.on('status', function(data) {
            $('#chat').val($('#chat').val() + '<' + data.msg + '>\n');
            $('#chat').scrollTop($('#chat')[0].scrollHeight);
        });
        socket.on('message', function(data) {
            $('#chat').val($('#chat').val() + data.msg + '\n');
            $('#chat').scrollTop($('#chat')[0].scrollHeight);
        });
        socket.on('delay', function(data) {
            setTimeout(update_chat_func(data.msg), data.delay);
        });
        $('#text').keypress(function(e) {
            var code = e.keyCode || e.which;
            if (code == 13) {
                send_msg();
            }
        });

    });
    function update_chat_func(msg) {
        return function() {
            $('#chat').val($('#chat').val() + msg + '\n');
            $('#chat').scrollTop($('#chat')[0].scrollHeight);
        }
    }
    function send_msg() {
        text = $('#text').val();
        if (text != '') {
            if (text.length > 200) {
                show_error();
            }
            else {
            hide_error();
            $('#text').val('');
            socket.emit('text', {msg: text});
            }
        }
    }
    function hide_error() {
    $('#msg-error').hide();
    }
    function show_error() {
        $('#msg-error').show();
    }
    function leave_room() {
        socket.emit('left', {}, function() {
            socket.disconnect();

            // go back to the login page
            var getUrl = window.location;
            var baseUrl = getUrl.protocol + "//" + getUrl.host + "/";
            window.location.href = baseUrl;
        });
    }