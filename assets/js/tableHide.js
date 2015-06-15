jQuery(function() {
   jQuery('table.tg input').on('click', function(event) {
        console.log('clicked');
        var th = event.currentTarget.parentElement,
            tr = th.parentElement,
            index = 0,
            child = tr.firstChild;

        while((child = child.nextSibling) != null) {
            if (child != th){
                index++;
            } else {
                break;
            }
        }

       jQuery('table tr').each(function() {
           var i = 0,
               child = this.firstChild;

           while (((child = child.nextSibling) != null) && (i < index)) {
               i++;
           }
           child.remove();
       });
    });
});
