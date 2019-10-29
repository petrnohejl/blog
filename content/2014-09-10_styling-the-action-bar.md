Title: Styling the Action Bar
Category: Android

Styling the Action Bar is complicated. There are a lot of attributes you can customize and it can take some time to set it up as you need. In this article I am going to show you how to create custom style of the Action Bar within 5 minutes.

There is a great tool [Android Action Bar Style Generator](https://jgilfelt.github.io/android-actionbarstylegenerator/) from Jeff Gilfelt. This web utility allows you to create a simple Action Bar style including nine patch PNG assets, XML drawables and XML styles. This is perfect but the generated XML theme is quite simple and there are some unresolved issues (e.g. indeterminate progress bar size). Also the naming convention of the assets and styles is inconsistent and little confusing for me. So I've created [Action Bar style template](https://github.com/petrnohejl/Android-Templates-And-Utilities/tree/master/Res-Style), which is more elaborated. I use this template in all my Android projects.

[Action Bar style template](https://github.com/petrnohejl/Android-Templates-And-Utilities/tree/master/Res-Style) contains all necessary files - PNG assets, XML drawables, colors, dimens, styles. It is based on [AppCompat library](https://developer.android.com/tools/support-library/features.html). Custom Action Bar style covers almost all customizable attributes. You can easily change the attributes, colors, dimens as you need. To colorize UI elements you can generate PNG assets using Android Action Bar Style Generator and copy them into the project.

Instructions how to use my Action Bar style template:

1. Copy & paste all files in [Res-Style](https://github.com/petrnohejl/Android-Templates-And-Utilities/tree/master/Res-Style) into your project (exclude _extras directory).
2. Open values/styles.xml, values-v11/styles.xml, values-v14/styles.xml and replace all occurences of "Example" to your own style name.
3. Visit [Android Action Bar Style Generator](https://jgilfelt.github.io/android-actionbarstylegenerator/) and generate colorized PNG assets.
4. Copy & paste \_extras/rename.bat into all drawable directories (which contains PNG files) generated via Android Action Bar Style Generator.
5. Run rename.bat scripts. It will just rename PNG files to make file names more clear and consistent. All assets are prefixed with "ab" (means Action Bar).
6. Copy & paste all PNG drawable files into your project. Some files are not necessary.
7. Done. Now you can customize and edit styles.xml, colors.xml, dimens.xml as you need.

See example screenshots:

![Action Bar with indeterminate progress bar]({filename}images/styling-action-bar-01.png)
![Tab navigation]({filename}images/styling-action-bar-02.png)
![List navigation]({filename}images/styling-action-bar-03.png)
![Action mode]({filename}images/styling-action-bar-04.png)

You can find source code on my GitHub in [Android Templates and Utilities](https://github.com/petrnohejl/Android-Templates-And-Utilities/tree/master/Res-Style) repo. Gotta some questions or ideas about styling the Action Bar? Follow me on [Twitter](https://twitter.com/petrnohejl) or [Google Plus](https://plus.google.com/113883771155661250237).
