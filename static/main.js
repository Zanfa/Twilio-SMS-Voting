function Voting() {
    var docEl = document.documentElement;
    //this._canvas = $('canvas');
    this._votes = {
        A: 0,
        B: 0
    };

    // Set the canvas to fill the window
    //this._canvas.width(docEl.clientWidth).height(docEl.clientHeight);
    this._draw();
}

Voting.prototype._update = function () {
    var t = this;

    $.getJSON("/json", function (json) {
        t._votes = json;
        t._draw();
    });
};

Voting.prototype._draw = function () {
    var elem, votes, candidate, progress, t;
    t = this;


    for (candidate in this._votes) {
        if (!this._votes.hasOwnProperty(candidate))
            continue;

        elem = $('#candidate' + candidate);
        votes = this._votes[candidate];

        progress = Math.round((votes / 50 * 100));

        elem.find('.votes').text(votes);
        elem.find('.progress').css('width',  + ((progress > 0) ? progress : 1) + "%");

        setTimeout(function () {
            t._update();
        }, 1000);
    }
};

$(function () {
    new Voting();
});
