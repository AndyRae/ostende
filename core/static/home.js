var isDateSupported = function () {
	var input = document.createElement('input');
	var value = 'a';
	input.setAttribute('type', 'date');
	input.setAttribute('value', value);
	return (input.value !== value);
};

if (isDateSupported()) {
	// Browser native date pickers are supported
  $(".safari-date-picker").hide();
}

if (!isDateSupported()) {
	// No support.
  $(".html5-date-picker").hide();      
}

Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#whatson',
  delimiters: ['${','}'],
  data: {
	screenings: [],
	message: null,
	search_term: '',
   },
   mounted: function() {
   this.getScreenings();
   },
	methods: {
	  getScreenings: function() {
		let api_url = '/api/screening/';
		if(this.search_term!==''||this.search_term!==null) {
		  api_url = `/api/screening/?search=${this.search_term}`
		}
		this.$http.get(api_url)
		 .then((response) => {
		 this.screenings = response.data.results;
		})
		.catch((err) => {
		  console.log(err);
		})
	   },
	 }

});