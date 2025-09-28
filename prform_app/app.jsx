import React, { useState, useEffect } from 'react';
import { Activity, AlertTriangle, CheckCircle, Zap, Users, TrendingUp, Settings, Play, Pause, RotateCcw, ArrowRight, Shield, Target, Award, ChevronRight } from 'lucide-react';

const FormGuardApp = () => {
  const [currentScreen, setCurrentScreen] = useState('welcome');
  const [userData, setUserData] = useState({
    name: '',
    email: '',
    password: '',
    experience: '',
    goals: [],
    injuries: []
  });
  const [activeExercise, setActiveExercise] = useState('bench-press');
  const [isTracking, setIsTracking] = useState(false);
  const [formScore, setFormScore] = useState(87);
  const [currentRep, setCurrentRep] = useState(0);
  const [alerts, setAlerts] = useState([]);
  const [sensorData, setSensorData] = useState({
    leftWrist: { status: 'good', angle: 45 },
    rightWrist: { status: 'good', angle: 47 },
    leftElbow: { status: 'warning', angle: 85 },
    rightElbow: { status: 'good', angle: 90 },
    symmetry: 94
  });

  const exercises = {
    'bench-press': { 
      name: 'Bench Press', 
      riskLevel: 'High', 
      targetReps: 8,
      feedback: [
        'Keep shoulder blades retracted',
        'Bar path should be straight up and down',
        'Lower the bar to mid-chest level',
        'Drive through your heels',
        'Maintain arch in lower back'
      ],
      warnings: [
        'Elbows flaring too wide - risk of shoulder impingement',
        'Bar drifting forward - maintain control',
        'Bouncing off chest - control the descent',
        'Uneven bar position - check grip symmetry',
        'Lifting hips off bench - maintain contact'
      ]
    },
    'squat': { 
      name: 'Back Squat', 
      riskLevel: 'High', 
      targetReps: 10,
      feedback: [
        'Keep chest up and core engaged',
        'Track knees over toes',
        'Reach proper depth - hips below knees',
        'Drive through heels on ascent',
        'Maintain neutral spine'
      ],
      warnings: [
        'Knees caving inward - activate glutes',
        'Forward lean detected - engage core more',
        'Insufficient depth - go lower',
        'Weight shifting to toes - stay on heels',
        'Knee tracking outside toe line'
      ]
    },
    'deadlift': { 
      name: 'Deadlift', 
      riskLevel: 'High', 
      targetReps: 5,
      feedback: [
        'Start with bar over mid-foot',
        'Keep back straight and chest up',
        'Drive through heels and squeeze glutes',
        'Bar should stay close to body',
        'Finish with hips fully extended'
      ],
      warnings: [
        'Rounding in lower back - reduce weight',
        'Bar drifting away from body',
        'Hyperextending at top - stop at neutral',
        'Uneven bar lift - check hand position',
        'Not engaging lats - pull bar to body'
      ]
    },
    'shoulder-press': { 
      name: 'Shoulder Press', 
      riskLevel: 'Medium', 
      targetReps: 12,
      feedback: [
        'Press straight up overhead',
        'Keep core tight throughout',
        'Start with weights at shoulder level',
        'Control the descent',
        'Full range of motion'
      ],
      warnings: [
        'Pressing forward instead of up',
        'Arching back excessively - engage core',
        'Uneven press detected',
        'Not reaching full extension overhead',
        'Elbows dropping too low on descent'
      ]
    }
  };

  const updateUserData = (field, value) => {
    setUserData(prev => ({ ...prev, [field]: value }));
  };

  const toggleGoal = (goal) => {
    setUserData(prev => ({
      ...prev,
      goals: prev.goals.includes(goal) 
        ? prev.goals.filter(g => g !== goal)
        : [...prev.goals, goal]
    }));
  };

  const toggleInjury = (injury) => {
    setUserData(prev => ({
      ...prev,
      injuries: prev.injuries.includes(injury) 
        ? prev.injuries.filter(i => i !== injury)
        : [...prev.injuries, injury]
    }));
  };

  useEffect(() => {
    if (isTracking) {
      const interval = setInterval(() => {
        const newScore = Math.max(60, Math.min(100, formScore + (Math.random() - 0.5) * 10));
        setFormScore(Math.round(newScore));
        
        const currentExercise = exercises[activeExercise];
        const feedbackMessages = currentExercise.feedback;
        const warningMessages = currentExercise.warnings;
        
        if (Math.random() < 0.7) {
          let newAlert;
          
          if (newScore < 70) {
            newAlert = {
              id: Date.now(),
              type: 'warning',
              message: warningMessages[Math.floor(Math.random() * warningMessages.length)],
              timestamp: new Date().toLocaleTimeString(),
              severity: 'high'
            };
          } else if (newScore < 85) {
            newAlert = {
              id: Date.now(),
              type: 'correction',
              message: feedbackMessages[Math.floor(Math.random() * feedbackMessages.length)],
              timestamp: new Date().toLocaleTimeString(),
              severity: 'medium'
            };
          } else if (Math.random() < 0.4) {
            const positiveMessages = [
              'Excellent form! Keep it up',
              'Perfect rep - maintain this technique',
              'Great control on that rep',
              'Solid form - you\'re in the zone',
              'Outstanding technique!'
            ];
            newAlert = {
              id: Date.now(),
              type: 'positive',
              message: positiveMessages[Math.floor(Math.random() * positiveMessages.length)],
              timestamp: new Date().toLocaleTimeString(),
              severity: 'low'
            };
          }
          
          if (newAlert) {
            setAlerts(prev => [newAlert, ...prev.slice(0, 4)]);
          }
        }
        
        if (Math.random() < 0.15 && currentRep < currentExercise.targetReps) {
          setCurrentRep(prev => prev + 1);
        }
        
        setSensorData(prev => {
          let newSensorData = { ...prev };
          
          switch(activeExercise) {
            case 'bench-press':
              newSensorData.leftWrist.angle = Math.round(45 + (Math.random() - 0.5) * 15);
              newSensorData.rightWrist.angle = Math.round(47 + (Math.random() - 0.5) * 15);
              newSensorData.leftElbow.angle = Math.round(85 + (Math.random() - 0.5) * 20);
              newSensorData.rightElbow.angle = Math.round(90 + (Math.random() - 0.5) * 20);
              break;
            case 'squat':
              newSensorData.leftWrist.angle = Math.round(180 + (Math.random() - 0.5) * 10);
              newSensorData.rightWrist.angle = Math.round(180 + (Math.random() - 0.5) * 10);
              newSensorData.leftElbow.angle = Math.round(90 + (Math.random() - 0.5) * 30);
              newSensorData.rightElbow.angle = Math.round(90 + (Math.random() - 0.5) * 30);
              break;
            case 'deadlift':
              newSensorData.leftWrist.angle = Math.round(180 + (Math.random() - 0.5) * 5);
              newSensorData.rightWrist.angle = Math.round(180 + (Math.random() - 0.5) * 5);
              newSensorData.leftElbow.angle = Math.round(170 + (Math.random() - 0.5) * 15);
              newSensorData.rightElbow.angle = Math.round(170 + (Math.random() - 0.5) * 15);
              break;
            case 'shoulder-press':
              newSensorData.leftWrist.angle = Math.round(0 + (Math.random() - 0.5) * 20);
              newSensorData.rightWrist.angle = Math.round(0 + (Math.random() - 0.5) * 20);
              newSensorData.leftElbow.angle = Math.round(90 + (Math.random() - 0.5) * 25);
              newSensorData.rightElbow.angle = Math.round(90 + (Math.random() - 0.5) * 25);
              break;
          }
          
          Object.keys(newSensorData).forEach(joint => {
            if (joint !== 'symmetry') {
              if (newScore < 70) {
                newSensorData[joint].status = 'danger';
              } else if (newScore < 85) {
                newSensorData[joint].status = 'warning';
              } else {
                newSensorData[joint].status = 'good';
              }
            }
          });
          
          newSensorData.symmetry = Math.max(75, Math.min(100, prev.symmetry + (Math.random() - 0.5) * 8));
          
          return newSensorData;
        });
      }, 1500);
      
      return () => clearInterval(interval);
    }
  }, [isTracking, formScore, activeExercise, currentRep]);

  const startTracking = () => {
    setIsTracking(true);
    setCurrentRep(0);
    setAlerts([]);
    const currentExercise = exercises[activeExercise];
    const initialAlert = {
      id: Date.now(),
      type: 'coaching',
      message: `Starting ${currentExercise.name} - ${currentExercise.feedback[0]}`,
      timestamp: new Date().toLocaleTimeString(),
      severity: 'low'
    };
    setAlerts([initialAlert]);
  };

  const stopTracking = () => {
    setIsTracking(false);
  };

  const getSensorStatusColor = (status) => {
    switch(status) {
      case 'good': return 'text-green-500';
      case 'warning': return 'text-yellow-500';
      case 'danger': return 'text-red-500';
      default: return 'text-gray-500';
    }
  };

  const getFormScoreColor = (score) => {
    if (score >= 85) return 'text-green-500';
    if (score >= 70) return 'text-yellow-500';
    return 'text-red-500';
  };

  const getAlertColor = (alert) => {
    switch(alert.type) {
      case 'warning': return 'bg-red-900 border-red-700';
      case 'correction': return 'bg-yellow-900 border-yellow-700';
      case 'positive': return 'bg-green-900 border-green-700';
      case 'coaching': return 'bg-blue-900 border-blue-700';
      default: return 'bg-yellow-900 border-yellow-700';
    }
  };

  const getAlertIcon = (alert) => {
    switch(alert.type) {
      case 'warning': return <AlertTriangle className="w-5 h-5 text-red-400 mt-0.5" />;
      case 'correction': return <AlertTriangle className="w-5 h-5 text-yellow-400 mt-0.5" />;
      case 'positive': return <CheckCircle className="w-5 h-5 text-green-400 mt-0.5" />;
      case 'coaching': return <Target className="w-5 h-5 text-blue-400 mt-0.5" />;
      default: return <AlertTriangle className="w-5 h-5 text-yellow-400 mt-0.5" />;
    }
  };

  if (currentScreen === 'welcome') {
    return (
      <div className="w-full max-w-sm mx-auto bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 text-white h-screen flex flex-col overflow-hidden">
        <div className="flex-1 flex flex-col justify-center items-center text-center px-8 py-12">
          <h1 className="text-4xl font-bold mb-4">PRFORM</h1>
          <p className="text-xl mb-3 text-purple-200">Precision in Every Rep</p>
          <p className="text-sm text-purple-300 mb-8 leading-relaxed">AI-powered real-time coaching to prevent injuries and maximize gains</p>
          
          <div className="space-y-6 mb-12 w-full">
            <div className="flex items-center gap-4 text-left">
              <Shield className="w-6 h-6 text-green-400 flex-shrink-0" />
              <span className="text-sm">Prevent 500K+ annual gym injuries</span>
            </div>
            <div className="flex items-center gap-4 text-left">
              <Target className="w-6 h-6 text-blue-400 flex-shrink-0" />
              <span className="text-sm">Real-time form correction</span>
            </div>
            <div className="flex items-center gap-4 text-left">
              <Award className="w-6 h-6 text-yellow-400 flex-shrink-0" />
              <span className="text-sm">Maximize your workout gains</span>
            </div>
          </div>
        </div>
        
        <div className="px-8 pb-8 space-y-4">
          <button 
            onClick={() => setCurrentScreen('signup')}
            className="w-full bg-white text-purple-900 font-semibold py-4 rounded-xl hover:bg-gray-100 transition-colors"
          >
            Get Started
          </button>
          <button 
            onClick={() => setCurrentScreen('login')}
            className="w-full border-2 border-white text-white font-semibold py-4 rounded-xl hover:bg-white hover:text-purple-900 transition-colors"
          >
            Sign In
          </button>
        </div>
      </div>
    );
  }

  if (currentScreen === 'signup') {
    return (
      <div className="w-full max-w-sm mx-auto bg-black text-white h-screen overflow-auto">
        <div className="p-6 h-full flex flex-col">
          <div className="flex items-center gap-3 mb-8">
            <h1 className="text-xl font-bold">PRFORM</h1>
          </div>
          
          <h2 className="text-2xl font-bold mb-6">Create Account</h2>
          
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-2">Full Name</label>
              <input
                type="text"
                value={userData.name}
                onChange={(e) => updateUserData('name', e.target.value)}
                className="w-full bg-gray-900 border border-gray-700 rounded-lg p-3 text-white focus:border-purple-500 focus:outline-none"
                placeholder="Enter your name"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium mb-2">Email</label>
              <input
                type="email"
                value={userData.email}
                onChange={(e) => updateUserData('email', e.target.value)}
                className="w-full bg-gray-900 border border-gray-700 rounded-lg p-3 text-white focus:border-purple-500 focus:outline-none"
                placeholder="Enter your email"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium mb-2">Password</label>
              <input
                type="password"
                value={userData.password}
                onChange={(e) => updateUserData('password', e.target.value)}
                className="w-full bg-gray-900 border border-gray-700 rounded-lg p-3 text-white focus:border-purple-500 focus:outline-none"
                placeholder="Create a password"
              />
            </div>
          </div>
          
          <button 
            onClick={() => setCurrentScreen('experience')}
            className="w-full bg-purple-600 font-semibold py-4 rounded-xl hover:bg-purple-700 transition-colors mt-8"
          >
            Continue <ArrowRight className="w-4 h-4 inline ml-2" />
          </button>
          
          <p className="text-center text-gray-400 text-sm mt-6">
            Already have an account? 
            <button 
              onClick={() => setCurrentScreen('login')}
              className="text-purple-400 hover:text-purple-300 ml-1"
            >
              Sign in
            </button>
          </p>
        </div>
      </div>
    );
  }

  if (currentScreen === 'login') {
    return (
      <div className="w-full max-w-sm mx-auto bg-black text-white h-screen overflow-auto">
        <div className="p-6 h-full flex flex-col">
          <div className="flex items-center gap-3 mb-8">
            <h1 className="text-xl font-bold">PRFORM</h1>
          </div>
          
          <h2 className="text-2xl font-bold mb-6">Welcome Back</h2>
          
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-2">Email</label>
              <input
                type="email"
                className="w-full bg-gray-900 border border-gray-700 rounded-lg p-3 text-white focus:border-purple-500 focus:outline-none"
                placeholder="Enter your email"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium mb-2">Password</label>
              <input
                type="password"
                className="w-full bg-gray-900 border border-gray-700 rounded-lg p-3 text-white focus:border-purple-500 focus:outline-none"
                placeholder="Enter your password"
              />
            </div>
          </div>
          
          <button 
            onClick={() => setCurrentScreen('main')}
            className="w-full bg-purple-600 font-semibold py-4 rounded-xl hover:bg-purple-700 transition-colors mt-8"
          >
            Sign In <ArrowRight className="w-4 h-4 inline ml-2" />
          </button>
          
          <p className="text-center text-gray-400 text-sm mt-6">
            Don't have an account? 
            <button 
              onClick={() => setCurrentScreen('signup')}
              className="text-purple-400 hover:text-purple-300 ml-1"
            >
              Sign up
            </button>
          </p>
        </div>
      </div>
    );
  }

  if (currentScreen === 'experience') {
    return (
      <div className="w-full max-w-sm mx-auto bg-black text-white h-screen overflow-auto">
        <div className="p-6 h-full flex flex-col">
          <div className="flex items-center gap-3 mb-8">
            <h1 className="text-xl font-bold">PRFORM</h1>
          </div>
          
          <h2 className="text-2xl font-bold mb-2">What's your gym experience?</h2>
          <p className="text-gray-400 mb-8">This helps us customize your form coaching</p>
          
          <div className="space-y-4">
            {[
              { level: 'beginner', title: 'Beginner', desc: 'New to the gym or returning after a break' },
              { level: 'intermediate', title: 'Intermediate', desc: '6 months - 2 years of consistent training' },
              { level: 'advanced', title: 'Advanced', desc: '2+ years of serious training experience' },
              { level: 'expert', title: 'Expert/Competitor', desc: 'Competitive athlete or trainer' }
            ].map((option) => (
              <button
                key={option.level}
                onClick={() => {
                  updateUserData('experience', option.level);
                  setCurrentScreen('goals');
                }}
                className={`w-full text-left p-4 rounded-xl border-2 transition-colors ${
                  userData.experience === option.level
                    ? 'border-purple-500 bg-purple-900'
                    : 'border-gray-700 bg-gray-900 hover:border-gray-600'
                }`}
              >
                <div className="flex items-center justify-between">
                  <div>
                    <h3 className="font-semibold">{option.title}</h3>
                    <p className="text-sm text-gray-400">{option.desc}</p>
                  </div>
                  <ChevronRight className="w-5 h-5 text-gray-400" />
                </div>
              </button>
            ))}
          </div>
        </div>
      </div>
    );
  }

  if (currentScreen === 'goals') {
    return (
      <div className="w-full max-w-sm mx-auto bg-black text-white h-screen overflow-auto">
        <div className="p-6 h-full flex flex-col">
          <div className="flex items-center gap-3 mb-8">
            <h1 className="text-xl font-bold">PRFORM</h1>
          </div>
          
          <h2 className="text-2xl font-bold mb-2">What are your goals?</h2>
          <p className="text-gray-400 mb-8">Select all that apply</p>
          
          <div className="space-y-3 mb-8">
            {[
              { id: 'injury-prevention', title: 'Injury Prevention', icon: Shield },
              { id: 'strength-building', title: 'Build Strength', icon: Target },
              { id: 'muscle-building', title: 'Build Muscle', icon: Award },
              { id: 'weight-loss', title: 'Lose Weight', icon: TrendingUp },
              { id: 'athletic-performance', title: 'Athletic Performance', icon: Zap },
              { id: 'general-fitness', title: 'General Fitness', icon: Activity }
            ].map((goal) => {
              const IconComponent = goal.icon;
              return (
                <button
                  key={goal.id}
                  onClick={() => toggleGoal(goal.id)}
                  className={`w-full text-left p-4 rounded-xl border-2 transition-colors ${
                    userData.goals.includes(goal.id)
                      ? 'border-purple-500 bg-purple-900'
                      : 'border-gray-700 bg-gray-900 hover:border-gray-600'
                  }`}
                >
                  <div className="flex items-center gap-3">
                    <IconComponent className="w-5 h-5 text-purple-400" />
                    <span className="font-medium">{goal.title}</span>
                  </div>
                </button>
              );
            })}
          </div>
          
          <button 
            onClick={() => setCurrentScreen('injuries')}
            className="w-full bg-purple-600 font-semibold py-4 rounded-xl hover:bg-purple-700 transition-colors"
          >
            Continue <ArrowRight className="w-4 h-4 inline ml-2" />
          </button>
        </div>
      </div>
    );
  }

  if (currentScreen === 'injuries') {
    return (
      <div className="w-full max-w-sm mx-auto bg-black text-white h-screen overflow-auto">
        <div className="p-6 h-full flex flex-col">
          <div className="flex items-center gap-3 mb-8">
            <h1 className="text-xl font-bold">PRFORM</h1>
          </div>
          
          <h2 className="text-2xl font-bold mb-2">Any past injuries?</h2>
          <p className="text-gray-400 mb-8">We'll be extra careful with these areas</p>
          
          <div className="space-y-3 mb-8">
            {[
              'Lower back',
              'Shoulders',
              'Knees',
              'Wrists',
              'Elbows',
              'Neck',
              'Ankles',
              'None'
            ].map((injury) => (
              <button
                key={injury}
                onClick={() => toggleInjury(injury)}
                className={`w-full text-left p-4 rounded-xl border-2 transition-colors ${
                  userData.injuries.includes(injury)
                    ? 'border-red-500 bg-red-900'
                    : 'border-gray-700 bg-gray-900 hover:border-gray-600'
                }`}
              >
                <div className="flex items-center gap-3">
                  <AlertTriangle className="w-5 h-5 text-red-400" />
                  <span className="font-medium">{injury}</span>
                </div>
              </button>
            ))}
          </div>
          
          <button 
            onClick={() => setCurrentScreen('main')}
            className="w-full bg-purple-600 font-semibold py-4 rounded-xl hover:bg-purple-700 transition-colors"
          >
            Start Training <ArrowRight className="w-4 h-4 inline ml-2" />
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="w-full max-w-sm mx-auto bg-black text-white min-h-screen relative">
      <div className="h-6 bg-black"></div>
      
      <div className="bg-gradient-to-r from-purple-900 to-blue-900 p-4 pb-6 rounded-b-xl">
        <div className="flex items-center justify-between mb-4">
          <h1 className="text-xl font-bold">PRFORM</h1>
          <Settings className="w-6 h-6 text-gray-300" />
        </div>
        
        <div className="mb-4">
          <label className="text-sm text-gray-300 mb-2 block">Current Exercise</label>
          <select 
            value={activeExercise} 
            onChange={(e) => setActiveExercise(e.target.value)}
            className="w-full bg-gray-800 border-0 rounded-xl p-4 text-white text-lg font-medium appearance-none"
          >
            {Object.entries(exercises).map(([key, exercise]) => (
              <option key={key} value={key}>{exercise.name}</option>
            ))}
          </select>
        </div>

        <div className="text-center bg-white bg-opacity-10 rounded-2xl p-6 backdrop-blur-sm">
          <div className={`text-5xl font-bold mb-2 ${getFormScoreColor(formScore)}`}>
            {formScore}%
          </div>
          <div className="text-sm text-gray-300">Form Score</div>
        </div>
      </div>

      <div className="p-4 bg-gray-900 mx-4 mt-4 rounded-2xl">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-3">
            <button 
              onClick={isTracking ? stopTracking : startTracking}
              className={`flex items-center gap-2 px-6 py-3 rounded-xl font-semibold text-white shadow-lg ${
                isTracking 
                  ? 'bg-red-500 hover:bg-red-600' 
                  : 'bg-green-500 hover:bg-green-600'
              }`}
            >
              {isTracking ? <Pause className="w-5 h-5" /> : <Play className="w-5 h-5" />}
              {isTracking ? 'Stop' : 'Start'}
            </button>
            <button className="p-3 bg-gray-700 rounded-xl hover:bg-gray-600">
              <RotateCcw className="w-5 h-5" />
            </button>
          </div>
          <div className="text-right">
            <div className="text-2xl font-bold">{currentRep}</div>
            <div className="text-xs text-gray-400">/ {exercises[activeExercise].targetReps} reps</div>
          </div>
        </div>

        <div className="flex items-center gap-2 bg-orange-500 bg-opacity-20 p-3 rounded-xl">
          <AlertTriangle className="w-5 h-5 text-orange-400" />
          <span className="text-sm font-medium">Risk Level: {exercises[activeExercise].riskLevel}</span>
        </div>
      </div>

      <div className="p-4 mx-4 mt-4 bg-gray-800 rounded-2xl">
        <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
          <Zap className="w-6 h-6 text-blue-400" />
          Sensor Status
        </h3>
        <div className="grid grid-cols-2 gap-3 mb-4">
          <div className="bg-gray-700 p-4 rounded-xl">
            <div className="text-xs text-gray-400 mb-1">Left Wrist</div>
            <div className={`text-lg font-bold ${getSensorStatusColor(sensorData.leftWrist.status)}`}>
              {Math.round(sensorData.leftWrist.angle)}°
            </div>
          </div>
          <div className="bg-gray-700 p-4 rounded-xl">
            <div className="text-xs text-gray-400 mb-1">Right Wrist</div>
            <div className={`text-lg font-bold ${getSensorStatusColor(sensorData.rightWrist.status)}`}>
              {Math.round(sensorData.rightWrist.angle)}°
            </div>
          </div>
          <div className="bg-gray-700 p-4 rounded-xl">
            <div className="text-xs text
            <div className="text-xs text-gray-400 mb-1">Left Elbow</div>
            <div className={`text-lg font-bold ${getSensorStatusColor(sensorData.leftElbow.status)}`}>
              {Math.round(sensorData.leftElbow.angle)}°
            </div>
          </div>
          <div className="bg-gray-700 p-4 rounded-xl">
            <div className="text-xs text-gray-400 mb-1">Right Elbow</div>
            <div className={`text-lg font-bold ${getSensorStatusColor(sensorData.rightElbow.status)}`}>
              {Math.round(sensorData.rightElbow.angle)}°
            </div>
          </div>
        </div>
        
        <div className="bg-gray-700 p-4 rounded-xl">
          <div className="text-xs text-gray-400 mb-2">Movement Symmetry</div>
          <div className="flex items-center gap-3">
            <div className="flex-1 bg-gray-600 rounded-full h-3">
              <div 
                className="bg-green-500 h-3 rounded-full transition-all duration-300 shadow-sm"
                style={{ width: `${sensorData.symmetry}%` }}
              ></div>
            </div>
            <span className="text-lg font-bold text-green-400">{Math.round(sensorData.symmetry)}%</span>
          </div>
        </div>
      </div>

      <div className="p-4 mx-4 mt-4">
        <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
          <AlertTriangle className="w-6 h-6 text-yellow-400" />
          Real-time Feedback
        </h3>
        <div className="space-y-3">
          {alerts.length === 0 ? (
            <div className="text-center py-8 bg-gray-800 rounded-2xl">
              <CheckCircle className="w-12 h-12 mx-auto mb-3 text-green-500" />
              <p className="text-gray-300 font-medium">Form looking good!</p>
              <p className="text-gray-400 text-sm">Keep up the great work</p>
            </div>
          ) : (
            alerts.map((alert) => (
              <div key={alert.id} className={`${getAlertColor(alert)} p-4 rounded-xl border-l-4`}>
                <div className="flex items-start gap-3">
                  {getAlertIcon(alert)}
                  <div className="flex-1">
                    <p className="font-medium text-white">{alert.message}</p>
                    <p className="text-xs text-gray-300 mt-1">{alert.timestamp}</p>
                  </div>
                </div>
              </div>
            ))
          )}
        </div>
      </div>

      <div className="p-4 mx-4 mt-4 mb-6 bg-gray-900 rounded-2xl">
        <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
          <TrendingUp className="w-6 h-6 text-green-400" />
          Today's Stats
        </h3>
        <div className="grid grid-cols-3 gap-4">
          <div className="text-center bg-green-500 bg-opacity-20 p-4 rounded-xl">
            <div className="text-2xl font-bold text-green-400">127</div>
            <div className="text-xs text-gray-400 mt-1">Total Reps</div>
          </div>
          <div className="text-center bg-blue-500 bg-opacity-20 p-4 rounded-xl">
            <div className="text-2xl font-bold text-blue-400">89%</div>
            <div className="text-xs text-gray-400 mt-1">Avg Form</div>
          </div>
          <div className="text-center bg-purple-500 bg-opacity-20 p-4 rounded-xl">
            <div className="text-2xl font-bold text-purple-400">3</div>
            <div className="text-xs text-gray-400 mt-1">Exercises</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FormGuardApp;
