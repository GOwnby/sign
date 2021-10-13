$('document').ready(function(){

const selection = new SelectionArea({

    // document object - if you want to use it within an embed document (or iframe).
    document: window.document,

    // Class for the selection-area element.
    class: 'selection-area',

    // Query selector or dom-node to set up container for the selection-area element.
    container: 'body',

    // Query selectors for elements which can be selected.
    selectables: [],

    // Query selectors for elements from where a selection can be started from.
    startareas: ['html'],

    // Query selectors for elements which will be used as boundaries for the selection.
    boundaries: ['html'],

    // px, how many pixels the point should move before starting the selection (combined distance).
    // Or specifiy the threshold for each axis by passing an object like {x: <number>, y: <number>}.
    startThreshold: 10,

    // Enable / disable touch support
    allowTouch: true,

    // On which point an element should be selected.
    // Available modes are cover (cover the entire element), center (touch the center) or
    // the default mode is touch (just touching it).
    intersect: 'touch',

    // Specifies what should be done if already selected elements get selected again.
    //   invert: Invert selection for elements which were already selected
    //   keep: Make stored elements (by keepSelectio()) 'fix'
    //   drop: Remove stored elements after they have been touched
    overlap: 'invert',

    // Configuration in case a selectable gets just clicked.
    singleTap: {

        // Enable single-click selection (Also disables range-selection via shift + ctrl).
        allow: true,

        // 'native' (element was mouse-event target) or 'touch' (element visually touched).
        intersect: 'native'
    },

    // Scroll configuration.
    scrolling: {

        // On scrollable areas the number on px per frame is devided by this amount.
        // Default is 10 to provide a enjoyable scroll experience.
        speedDivider: 10,

        // Browsers handle mouse-wheel events differently, this number will be used as 
        // numerator to calculate the mount of px while scrolling manually: manualScrollSpeed / scrollSpeedDivider.
        manualSpeed: 750
    }
});
});