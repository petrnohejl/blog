Title: Handling bundles in activities and fragments
Category: Android

[Bundle](http://developer.android.com/reference/android/os/Bundle.html) is a useful data holder, which maps String values to various [Parcelable](http://developer.android.com/reference/android/os/Parcelable.html) types. So basically it is a heterogenous key/value map. Bundles are used in [Intents](http://developer.android.com/reference/android/content/Intent.html), [Activities](http://developer.android.com/reference/android/app/Activity.html) and [Fragments](http://developer.android.com/reference/android/app/Fragment.html) for transporting data. I would like to describe how I work with Bundles on Android and show you some good tips.

## Activity

When you are creating a new instance of Activity via Intent, you can pass some extra data to the Activity. Data are stored in Bundle and can be retrieved by calling `getIntent().getExtras()`. It's a good practise to implement static method `newIntent()` which returns a new Intent that can be used to start the Activity. This way you have compile time checking for the arguments passed to the Activity. This pattern is suitable for Service and Broadcast as well.

Bundle is also used if the Activity is being re-initialized (e.g. because of configuration changes) for keeping the current state of the instance. You can supply some data in `onSaveInstanceState(Bundle)` and retrieve them back in `onCreate(Bundle)` method or `onRestoreInstanceState(Bundle)`. Main difference between these methods is that `onRestoreInstanceState(Bundle)` is called after `onStart()`. Sometimes it's convenient to restore data here after all of the initialization has been done. Another purpose could be allowing subclasses to decide whether to use your default implementation.

See example code below. Note that `EXTRA_PRODUCT_ID` constant is public. That's because we could need it in a Fragment encapsulated in this Activity.

    :::java
    public class ExampleActivity extends Activity
	{
		public static final String EXTRA_PRODUCT_ID = "product_id";
		public static final String EXTRA_PRODUCT_TITLE = "product_title";

		private static final String SAVED_PAGER_POSITION = "pager_position";

		public static Intent newIntent(Context context, String productId, String productTitle)
		{
			Intent intent = new Intent(context, ExampleActivity.class);

			// extras
			intent.putExtra(EXTRA_PRODUCT_ID, productId);
			intent.putExtra(EXTRA_PRODUCT_TITLE, productTitle);

			return intent;
		}

		@Override
		public void onCreate(Bundle savedInstanceState)
		{
			super.onCreate(savedInstanceState);
			setContentView(R.layout.activity_example);

			// restore saved state
			if(savedInstanceState != null)
			{
				handleSavedInstanceState(savedInstanceState);
			}

			// handle intent extras
			Bundle extras = getIntent().getExtras();
			if(extras != null)
			{
				handleExtras(extras);
			}
		}

		@Override
		public void onSaveInstanceState(Bundle outState)
		{
			// save current instance state
			super.onSaveInstanceState(outState);

			// TODO
		}

		@Override
		public void onRestoreInstanceState(Bundle savedInstanceState)
		{
			// restore saved state
			super.onRestoreInstanceState(savedInstanceState);

			if(savedInstanceState != null)
			{
				// TODO
			}
		}

		private void handleSavedInstanceState(Bundle savedInstanceState)
		{
			// TODO
		}

		private void handleExtras(Bundle extras)
		{
			// TODO
		}
	}

## Fragment

When you are creating a new instance of Fragment, you can pass arguments through `setArguments(Bundle)` method. Data can be retrieved with `getArguments()` method. It would be a mistake to supply initialization data through an overloaded constructor. Fragment instance can be re-created (e.g. because of configuration changes) so you would lose data, because constructor with extra parameters is not called when re-initializing Fragment. Only empty constructor is called. Best way to solve this problem is implementing static creator method `newInstance()` which returns a new instance of Fragment and sets the arguments via `setArguments(Bundle)`.

Fragment state can be saved using `onSaveInstanceState(Bundle)` method. It is similar to the Activity. Data can be restored in `onCreate(Bundle)`, `onCreateView(LayoutInflater, ViewGroup, Bundle)`, `onActivityCreated(Bundle)` or `onViewStateRestored(Bundle)` methods.

Fragment has also access to the Intent extras which were passed during creating the Activity instance. You can get this extra data by calling `getActivity().getIntent().getExtras()`.

See example code below.

	:::java
	public class ExampleFragment extends Fragment
	{
		private static final String ARGUMENT_PRODUCT_ID = "product_id";

		private static final String SAVED_LIST_POSITION = "list_position";

		public static ExampleFragment newInstance(String productId)
		{
			ExampleFragment fragment = new ExampleFragment();

			// arguments
			Bundle arguments = new Bundle();
			arguments.putString(ARGUMENT_PRODUCT_ID, productId);
			fragment.setArguments(arguments);

			return fragment;
		}

		public ExampleFragment() {}

		@Override
		public void onCreate(Bundle savedInstanceState) 
		{
			super.onCreate(savedInstanceState);

			// handle fragment arguments
			Bundle arguments = getArguments();
			if(arguments != null)
			{
				handleArguments(arguments);
			}

			// restore saved state
			if(savedInstanceState != null)
			{
				handleSavedInstanceState(savedInstanceState);
			}
			
			// handle intent extras
			Bundle extras = getActivity().getIntent().getExtras();
			if(extras != null)
			{
				handleExtras(extras);
			}
		}

		@Override
		public void onSaveInstanceState(Bundle outState)
		{
			// save current instance state
			super.onSaveInstanceState(outState);

			// TODO
		}

		private void handleArguments(Bundle arguments)
		{
			// TODO
		}

		private void handleSavedInstanceState(Bundle savedInstanceState)
		{
			// TODO
		}
		
		private void handleExtras(Bundle extras)
		{
			// TODO
		}
	}

You can find example code also on my GitHub in [Android Templates and Utilities](https://github.com/petrnohejl/Android-Templates-And-Utilities/tree/master/Src-Bundle) repo. This blogpost was inspired by [Nick Butcher's post](https://plus.google.com/u/0/+AndroidDevelopers/posts/bCD7Zvd945d) on Google Plus. Gotta some questions or ideas about Bundles? Follow me on [Twitter](https://twitter.com/petrnohejl) or [Google Plus](https://plus.google.com/113883771155661250237).
