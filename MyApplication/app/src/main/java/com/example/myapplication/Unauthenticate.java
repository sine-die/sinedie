package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Unauthenticate extends AppCompatActivity implements View.OnClickListener {

    Button businessButton, userButton;
    UserLocalStore userLocalStore;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_unauthenticate);

        businessButton = (Button) findViewById(R.id.business_btn);
        userButton = (Button) findViewById(R.id.user_btn);

        businessButton.setOnClickListener(this);
        userButton.setOnClickListener(this);

        userLocalStore = new UserLocalStore(this);
    }

/*
    @Override
    protected void onStart(){
        super.onStart();

        if (authenticate()) {

        }

    }
*/

    private boolean authenticate(){
        return userLocalStore.getUserLoggedIn();
    }

    @Override
    public void onClick(View v) {
        switch(v.getId()){
            case R.id.business_btn:
                startActivity(new Intent(this, Login.class));
                break;
            /*case R.id.user_btn:
                startActivity(new Intent(this, Login.class));
                break;*/
        }
    }

    /**
     * Called when the user taps the Send button

    public void sendMessage(View view) {
        Intent intent = new Intent(this, DisplayMessageActivity.class);
        EditText editText = (EditText) findViewById(R.id.editText);
        String message = editText.getText().toString();
        intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);
    }
     */
}