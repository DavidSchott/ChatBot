$(document).ready(function() {
    hide_on_init();
    // Carousel Select Event
    $('.radio').click(function() {
        // Highlight selection in Carousel
        $(this).find("input:radio").prop("checked", true);
        $('.highlight').removeClass("highlight");
        $(this).addClass("highlight");
        // Update value of room with corresponding #
        room = $(this).find("input:radio").val();
        name = $(this).find("p").html();
        show_bot_description(room, name);
        $('#room').val(room);
    })
});

/* Functions */
function hide_on_init(){
    $('#bot-selected-box').hide();
}
function show_bot_description(room, name){
    $('#bot-title').html("You selected: " + name);
    switch(room) {
        case '1':
            description = "<p>Worried about the eminent robot revolution? Connect with like-minded people in this public room.</p><strong>Tags: Public, Bot-free</strong>";
            break;
        case '10':
            description = "<p>Speak to the infamous Eliza Chatbot from the 60's.</p><strong>Tags: NLTK, Pattern-matching</strong>";
            break;
        case '20':
            description = "<p>Speak to Sun Tsu, an ancient, wise chinese military general and philosopher.</p><strong>Tags: NLTK, Pattern-matching, Random</strong>";
            break;
        case '30':
            description = "<p>Are you an anime fan? Then speak with this anime/manga obsessed bot! </p><strong>Tags: NLTK, Pattern-matching</strong>";
            break;
        case '40':
            description = "<p>Unlock life's hidden secrets by chatting to this expert on Zen Buddhism.</p><strong>Tags: NLTK, Pattern-matching, Random</strong>";
            break;
        case '50':
            description = "<p>Had a rough day? Why don't you let it all out on this bot. </p><strong>Tags: NLTK, Pattern-matching</strong>";
            break;
        case '60':
            description = "<p>This frequency-based bot will imitate speeches based on previous conversations. It gets reset when not in use for 30 minutes.</p><strong>Tags: Frequency-based, Evolving</strong>";
            break;
        case '70':
            description = "<p>This bot was trained on the <a href='http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html'>Cornell Movie Dialog</a> dataset. It still is a bit unstable on Heroku :(</p><strong>Tags: RNN, Seq2Seq, *NEW*</strong>";
            break;
        default:
            description = "<p>This bot is straight up awesome!</p>";
    }
    $('#bot-description').html(description);
    $('#bot-selected-box').show();
}