package com.example.getui;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;

import com.igexin.slavesdk.MessageManager;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends Activity implements OnClickListener {
	Button loginButton;
	EditText uid;
	EditText tid;
	EditText active_code;
	String s_uid;
	String s_tid;
	String s_active_code;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		loginButton = (Button) findViewById(R.id.button1);
		loginButton.setOnClickListener(this);
		uid = (EditText) findViewById(R.id.uid);
		tid = (EditText) findViewById(R.id.tid);
		active_code = (EditText) findViewById(R.id.active_code);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public void onClick(View v) {
		// TODO Auto-generated method stub
		if (v == loginButton) {
			// ��ȡ�û���������ֵ
			s_uid = uid.getText().toString();
			s_tid = tid.getText().toString();
			s_active_code = active_code.getText().toString();
			if (s_uid.equals("")) {
				Toast.makeText(this, "uid������Ϊ�գ�", Toast.LENGTH_SHORT).show();
				return;
			}
			if (s_tid.equals("")) {
				Toast.makeText(this, "uid������Ϊ��", Toast.LENGTH_SHORT).show();
				return;
			}
			if (s_active_code.equals("")) {
				Toast.makeText(this, "�����벻����Ϊ��", Toast.LENGTH_SHORT).show();
				return;
			}

			String baseURL = "http://10.0.2.2/android/enroll?tid=" + s_tid
					+ "&active_code=" + s_active_code + "&phone=" + s_uid;
			System.out.println(baseURL);
			HttpGet httpGet = new HttpGet(baseURL);
			HttpClient httpClient = new DefaultHttpClient();

			try {

				HttpResponse response = httpClient.execute(httpGet);

				// ��ʾ��Ӧ
				HttpEntity httpEntity = response.getEntity();
				InputStream inputStream = httpEntity.getContent();
				BufferedReader reader = new BufferedReader(
						new InputStreamReader(inputStream));
				String result = "";
				String line = "";
				while (null != (line = reader.readLine())) {
					result += line;

				}
				Toast.makeText(this, result, Toast.LENGTH_SHORT).show();
				Intent intent=new Intent();
		    	intent.setClass(MainActivity.this,getui.class);
		    	Bundle bundle=new Bundle();
		    	bundle.putString("uid", s_uid);//�û�ID
		    	bundle.putString("uname", s_tid);//�û���
		    	intent.putExtras(bundle);
		    	startActivity(intent);
		    	MainActivity.this.finish();//�رյ�ǰ��ͼ
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
}
