$(function() {

   
    Morris.Bar({
        element: 'morris-bar-chart',
   data: [{
            y: 'BFM',
            a: 20
            
        }, {
            y: 'BM',
            a: 75
        }, {
            y: 'KMP',
            a: 50
        }],
        xkey: 'y',
        ykeys: ['a'],
        labels: ['Character Count'],
        hideHover: 'auto',
        resize: true
    });
    
  
Morris.Bar({
        element: 'morris-bar-chart-2',
        data: [{
            y: 'BFM',
            a: 20
            
        }, {
            y: 'BM',
            a: 75
        }, {
            y: 'KMP',
            a: 50
        }],
        xkey: 'y',
        ykeys: ['a'],
        labels: ['Character Count'],
        hideHover: 'auto',
        resize: true
    });
    

    
Morris.Bar({
        element: 'morris-bar-chart-3',
        data: [{
            y: 'BFM',
            a: 20
            
        }, {
            y: 'BM',
            a: 75
        }, {
            y: 'KMP',
            a: 50
        }],
        xkey: 'y',
        ykeys: ['a'],
        labels: ['Character Count'],
        hideHover: 'auto',
        resize: true
    });
    


});
