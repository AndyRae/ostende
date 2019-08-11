Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#whatson',
  delimiters: ['${','}'],
  data: {
	screenings: [],
	message: null,
	urlparams: '',
   },
   mounted: function() {
   this.getScreenings();
   },
   methods: {
	getScreenings: function() {
	  let api_url = '/api/screeningdate/';
	  if(this.urlparams!==''||this.urlparams!==null) {
		api_url = `/api/screeningdate/`
	  }
	  this.$http.get(api_url)
	   .then((response) => {
	   this.screenings = response.data.results;
	  })
	  .catch((err) => {
		console.log(err);
	  })
	},
   },

});